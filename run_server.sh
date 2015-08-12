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
}

venv=.venv
with_venv=tools/with_venv.sh
always_venv=0
never_venv=0
no_site_packages=0
force=0
wrapper=""
update=0

if ! options=$(getopt -o VNnfuhd -l virtual-env,no-virtual-env,no-site-packages,force,update,help,debug -- "$@")
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
    esac
    shift
done

cd $(dirname "$0")

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

function run_server {
  ${wrapper} pecan serve config.py
}

run_server
