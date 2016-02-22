#!/bin/bash

function usage {
    echo "Usage: $0 [OPTION]..."
    echo "Migrate from the api-ref site into a from fairy-slipper"
    echo ""
    echo "  -V, --virtual-env        Always use virtualenv.  Install automatically if not present"
    echo "  -N, --no-virtual-env     Don't use virtualenv.  Run tests in local environment"
    echo "  -n, --no-site-packages   Isolate the virtualenv from the global Python environment"
    echo "  -f, --force              Force a clean re-build of the virtual environment. Useful when dependencies have been added."
    echo "  -u, --update             Update the virtual environment with any newer package versions"
    echo "  -h, --help               Print this usage message"
    echo "  -d, --debug              Run tests with testtools instead of testr. This allows you to use PDB"
    echo "  --docs-only              Only generate docs"
    echo "  --verbose-docs           Verbose logging of document generation"
    echo "  --docbkx2json            Only perform docbook to json conversion"
    echo "  --wadl2swagger           Only perform wadl to swagger-ish conversion"
    echo "  --wadl2swaggervalid      Only perform wadl to valid swagger conversion"
    echo "  --swagger2rst            Only perform swagger to rst conversion"
}

venv=.venv
with_venv=tools/with_venv.sh
always_venv=0
never_venv=0
no_site_packages=0
debug=0
force=0
wrapper=""
update=0
docs_only=
verbose_docs=""
docbkx2json=
wadl2swagger=
wadl2swaggervalid=
swagger2rst=

if ! options=$(getopt -o VNnfuhd -l virtual-env,no-virtual-env,no-site-packages,force,update,help,debug,docs-only,verbose-docs,docbkx2json,wadl2swagger,wadl2swaggervalid,swagger2rst -- "$@")
then
  # parse error
  usage
  exit 1
fi

eval set -- "$options"
while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help) usage; exit;;
        -V|--virtual-env) always_venv=1; never_venv=0;;
        -N|--no-virtual-env) always_venv=0; never_venv=1;;
        -n|--no-site-packages) no_site_packages=1;;
        -f|--force) force=1;;
        -u|--update) update=1;;
        -d|--debug) debug=1;;
        --docs-only) docs_only=1;;
        --verbose-docs) verbose_docs="-v";;
        --docbkx2json) docbkx2json=1;;
        --wadl2swagger) wadl2swagger=1;;
        --wadl2swaggervalid) wadl2swaggervalid=1;;
        --swagger2rst) swagger2rst=1;;
    esac
    shift
done

cd `dirname "$0"`

if [ $no_site_packages -eq 1 ]; then
  installvenvopts="--no-site-packages"
fi

if [ $never_venv -eq 0 ]
then
  # Remove the virtual environment if --force used
  if [ $force -eq 1 ]; then
    echo "Cleaning virtualenv..."
    rm -rf ${venv}
  fi
  if [ $update -eq 1 ]; then
    echo "Updating virtualenv..."
    python tools/install_venv.py $installvenvopts
  fi
  if [ -e ${venv} ]; then
    wrapper="${with_venv}"
  else
      if [ $always_venv -eq 1 ]; then
        # Automatically install the virtualenv
        python tools/install_venv.py $installvenvopts
        wrapper="${with_venv}"
      else
          echo -e "No virtual environment found...create one? (Y/n) \c"
          read use_ve
          if [ "x$use_ve" = "xY" -o "x$use_ve" = "x" -o "x$use_ve" = "xy" ]; then
            # Install the virtualenv and run the test suite in it
            python tools/install_venv.py $installvenvopts
            wrapper=${with_venv}
          fi
      fi
  fi
fi

function install_fairy_slipper {
  ${wrapper} pip install -e .
}

function install_api_site {
    if [ ! -d api-site ]; then
      git clone https://github.com/openstack/api-site.git
    fi
}

function migrate_docbkx {
    if [ ! -d conversion_files ]; then
      mkdir conversion_files
    fi
    if [ ! -d conversion_files_valid ]; then
      mkdir conversion_files_valid
    fi
    if [ ! -d api_doc ]; then
      mkdir api_doc
    fi

    generate_all=
    if [[ -z $docbkx2json && -z $wadl2swagger && -z $wadl2swaggervalid && -z $swagger2rst ]]; then
      generate_all=1
    fi

    if [[ -n $docbkx2json || -n $generate_all ]]; then
      ${wrapper} find api-site/api-ref/src/docbkx/ -name api-ref-\* -type f -exec fairy-slipper-docbkx-to-json -o conversion_files $verbose_docs {} \;
    fi

    if [[ -n $wadl2swagger || -n $generate_all ]]; then
      ${wrapper} find conversion_files -name api-ref\*json -type f -exec fairy-slipper-wadl-to-swagger -o conversion_files $verbose_docs {} \;
    fi

    if [[ -n $wadl2swaggervalid || -n $generate_all ]]; then
        ${wrapper} find conversion_files -name api-ref\*json -type f -exec fairy-slipper-wadl-to-swagger-valid -o conversion_files_valid $verbose_docs {} \;
    fi

    if [[ -n $swagger2rst || -n $generate_all ]]; then
      ${wrapper} find conversion_files_valid -name \*-swagger.json -type f -exec fairy-slipper-swagger-to-rst -o api_doc $verbose_docs {} \;
    fi
}

if [ -z $docs_only ]; then
  install_fairy_slipper
  install_api_site
fi

migrate_docbkx