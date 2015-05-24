#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging
import os
import re
import xml.sax
from os import path
import textwrap

import prettytable

log = logging.getLogger(__file__)


SECTIONS = {u'API_Versions': u'api-versions',
            u'Database_Instances': u'database-instances',
            u'admin-tenants': u'admin-tenants',
            u'admin-tokens': u'admin-tokens',
            u'admin-users': u'admin-users',
            u'admin-versions': u'admin-versions',
            u'alarms': u'alarms',
            u'build-info': u'build-info',
            u'capabilities': u'capabilities',
            u'compute_extensions': u'extensions',
            u'compute_flavors': u'flavors',
            u'compute_image_metadata': u'image-metadata',
            u'compute_images': u'images',
            u'compute_limits': u'limits',
            u'compute_server-actions': u'server-actions',
            u'compute_server-addresses': u'server-addresses',
            u'compute_server_metadata': u'server-metadata',
            u'compute_servers': u'servers',
            u'compute_versions': u'versions',
            u'credentials-v3': u'credentials',
            u'database-instance-actions': u'database-instance-actions',
            u'databases': u'databases',
            u'datastores': u'datastores',
            u'diagnostics-v2.1': u'diagnostics',
            u'domains-v3': u'domains',
            u'endpoints-v3': u'endpoints',
            u'ext-backups-v2': u'ext-backups',
            u'extraroute-ext': u'extraroute',
            u'flavor-extra-specs-v2.1': u'flavor-extra-specs',
            u'flavors': u'flavors',
            u'general-info': u'general-info',
            u'groups-v3': u'groups',
            u'heat-versions': u'heat-versions',
            u'identity-auth-v2': u'identity-auth',
            u'identity-v2-versions': u'versions',
            u'identity_v3_OS-INHERIT-ext': u'inherit',
            u'identity_v3_OS-KDS-ext': u'kds',
            u'identity_v3_OS-OAUTH1-ext': u'oauth1',
            u'identity_v3_OS-TRUST-ext': u'trust',
            u'image-data-v2': u'image-data',
            u'image-schemas-v2': u'image-schemas',
            u'image-tags-v2': u'image-tags',
            u'images-v1': u'images',
            u'images-v2': u'images',
            u'keypairs-v2.1': u'keypairs',
            u'layer3': u'layer3',
            u'lbaas-v1.0': u'lbaas',
            u'lbaas-v2.0': u'lbaas',
            u'limits-v2.1': u'limits',
            u'members-v1': u'members',
            u'members-v2': u'members',
            u'metering-ext': u'metering',
            u'meters': u'meters',
            u'network_multi_provider-ext': u'network-multi-provider',
            u'network_provider-ext': u'network-provider',
            u'network_vlan_transparency-ext': u'network-vlan-transparency',
            u'networks': u'networks',
            u'neutron-versions-v2': u'versions',
            u'neutron_extensions': u'extensions',
            u'os-admin-actions': u'admin-actions',
            u'os-admin-actions-v2.1': u'admin-actions',
            u'os-admin-password-v2.1': u'admin-password',
            u'os-agents': u'agents',
            u'os-agents-v2.1': u'agents',
            u'os-aggregates': u'aggregates',
            u'os-aggregates-v2.1': u'aggregates',
            u'os-availability-zone': u'availability-zone',
            u'os-availability-zone-v2.1': u'availability-zone',
            u'os-baremetal-ext-status': u'baremetal-ext-status',
            u'os-block-device-mapping-v2-boot': u'block-device-mapping',
            u'os-cells-v2.1': u'cells',
            u'os-certificates': u'certificates',
            u'os-certificates-v2.1': u'certificates',
            u'os-cloudpipe': u'cloudpipe',
            u'os-config-drive-v2.1': u'config-drive',
            u'os-console-output': u'console-output',
            u'os-console-output-v2.1': u'console-output',
            u'os-consoles': u'consoles',
            u'os-coverage': u'coverage',
            u'os-create-backup-v2.1': u'create-backup',
            u'os-createserverext': u'createserverext',
            u'os-deferred-delete': u'deferred-delete',
            u'os-deferred-delete-v2.1': u'deferred-delete',
            u'os-diagnostics': u'diagnostics',
            u'os-disk-config': u'disk-config',
            u'os-evacuate-v2.1': u'evacuate',
            u'os-ext-az': u'ext-az',
            u'os-ext-img-size': u'ext-img-size',
            u'os-ext-ips': u'ext-ips',
            u'os-extended-availability-zone-v2.1': u'extended-availability-zone',
            u'os-extended-networks': u'extended-networks',
            u'os-extended-server-attributes': u'extended-server-attributes',
            u'os-extended-server-attributes-v2.1': u'extended-server-attributes',
            u'os-extended-status': u'extended-status',
            u'os-extended-status-v2.1': u'extended-status',
            u'os-fixed-ips': u'fixed-ips',
            u'os-flavor-access': u'flavor-access',
            u'os-flavor-access-v2.1': u'flavor-access',
            u'os-flavor-extra-specs': u'flavor-extra-specs',
            u'os-flavor-manage-v2.1': u'flavor-manage',
            u'os-flavor-rxtx': u'flavor-rxtx',
            u'os-flavor-rxtx-v2.1': u'flavor-rxtx',
            u'os-flavor-swap': u'flavor-swap',
            u'os-flavorextradata': u'flavorextradata',
            u'os-flavormanage': u'flavormanage',
            u'os-flavors-v2.1': u'flavors',
            u'os-floating-ip-dns': u'floating-ip-dns',
            u'os-floating-ip-dns-v2.1': u'floating-ip-dns',
            u'os-floating-ip-pools': u'floating-ip-pools',
            u'os-floating-ip-pools-v2.1': u'floating-ip-pools',
            u'os-floating-ips': u'floating-ips',
            u'os-floating-ips-bulk': u'floating-ips-bulk',
            u'os-floating-ips-bulk-v2.1': u'floating-ips-bulk',
            u'os-floating-ips-v2.1': u'floating-ips',
            u'os-flv-disabled': u'flv-disabled',
            u'os-hosts': u'hosts',
            u'os-hosts-v2.1': u'hosts',
            u'os-hypervisor-status': u'hypervisor-status',
            u'os-hypervisors': u'hypervisors',
            u'os-hypervisors-v2.1': u'hypervisors',
            u'os-instance-actions': u'instance-actions',
            u'os-instance-actions-v2.1': u'instance-actions',
            u'os-instance-usage-audit-log-v2.1': u'instance-usage-audit-log',
            u'os-interface': u'interface',
            u'os-keypairs': u'keypairs',
            u'os-ksadm-admin-ext': u'ksadm-admin',
            u'os-kscatalog-ext': u'kscatalog',
            u'os-ksec2-admin-ext': u'ksec2-admin',
            u'os-kss3-admin-ext': u'kss3-admin',
            u'os-ksvalidate-ext': u'ksvalidate',
            u'os-limits-v2': u'limits',
            u'os-metadef-namespace-v2': u'metadef-namespace',
            u'os-metadef-object-v2': u'metadef-object',
            u'os-metadef-property-v2.wadl': u'metadef-property',
            u'os-metadef-resourcetype-v2': u'metadef-resourcetype',
            u'os-metadef-schemas-v2': u'metadef-schemas',
            u'os-metadef-tag-v2': u'metadef-tag',
            u'os-migrations': u'migrations',
            u'os-migrations-v2.1': u'migrations',
            u'os-multi-server-create': u'multi-server-create',
            u'os-multinic-v2.1': u'multinic',
            u'os-multiple-create-v2.1': u'multiple-create',
            u'os-networks': u'networks',
            u'os-networks-v2.1': u'networks',
            u'os-qos-v2-qos-specs': u'qos-v2-qos-specs',
            u'os-quota-class-sets': u'quota-class-sets',
            u'os-quota-class-sets-v2.1': u'quota-class-sets',
            u'os-quota-sets': u'quota-sets',
            u'os-quota-sets-v2': u'quota-sets',
            u'os-quota-sets-v2.1': u'quota-sets',
            u'os-remote-consoles-v2.1': u'remote-consoles',
            u'os-rescue': u'rescue',
            u'os-scheduler-hints': u'scheduler-hints',
            u'os-security-group-default-rules': u'security-group-default-rules',
            u'os-security-groups': u'security-groups',
            u'os-security-groups-v2.1': u'security-groups',
            u'os-server-OS-EXT-IPS-MAC': u'server-ext-ips-mac',
            u'os-server-actions-v2.1': u'server-actions',
            u'os-server-groups': u'server-groups',
            u'os-server-groups-v2.1': u'server-groups',
            u'os-server-password': u'server-password',
            u'os-server-password-v2.1': u'server-password',
            u'os-server-shelve': u'server-shelve',
            u'os-server-start-stop': u'server-start-stop',
            u'os-server-usage-v2.1': u'server-usage',
            u'os-services': u'services',
            u'os-services-v2.1': u'services',
            u'os-shelve-v2.1': u'shelve',
            u'os-simple-tenant-usage': u'simple-tenant-usage',
            u'os-tenant-networks-v2.1': u'tenant-networks',
            u'os-used-limits': u'used-limits',
            u'os-used-limits-for-admins': u'used-limits-for-admins',
            u'os-virtual-interfaces': u'virtual-interfaces',
            u'os-virtual-interfaces-v2.1': u'virtual-interfaces',
            u'os-volume': u'volume',
            u'os-volume-manage-v2': u'volume-manage',
            u'os-volume-type-access-v2': u'volume-type-access',
            u'os-volume_attachments': u'volume-attachments',
            u'policies-v3': u'policies',
            u'port_binding-ext': u'port-binding',
            u'ports': u'ports',
            u'projects-v3': u'projects',
            u'quotas-ext': u'quotas',
            u'resources': u'resources',
            u'roles-v3': u'roles',
            u'samples': u'samples',
            u'security_groups': u'security-groups',
            u'server-ips-v2.1': u'server-ips',
            u'service-catalog-v3': u'service-catalog',
            u'service-status': u'service-status',
            u'shared_images_v1': u'shared-images',
            u'software-config': u'software-config',
            u'stack-actions': u'stack-actions',
            u'stack-events': u'stack-events',
            u'stack-resources': u'stack-resources',
            u'stack-templates': u'stack-templates',
            u'stacks': u'stacks',
            u'storage_account_services': u'storage-account-services',
            u'storage_container_services': u'storage-container-services',
            u'storage_object_services': u'storage-object-services',
            u'subnets': u'subnets',
            u'tokens-v3': u'tokens',
            u'user_management': u'user-management',
            u'users-v3': u'users',
            u'v1.1clusters': u'clusters',
            u'v1.1clustertemplate': u'clustertemplate',
            u'v1.1datasources': u'datasources',
            u'v1.1event-log': u'event-log',
            u'v1.1imageregistry': u'imageregistry',
            u'v1.1jobbinaries': u'jobbinaries',
            u'v1.1jobbinary-internals': u'jobbinary-internals',
            u'v1.1jobexecutions': u'job-executions',
            u'v1.1jobs': u'jobs',
            u'v1.1jobtypes': u'job-types',
            u'v1.1nodegrouptemplate': u'node-group-template',
            u'v1.1plugins': u'plugins',
            u'v2.1os-fping': u'fping',
            u'versions-identity-v3': u'versions-identity',
            u'versions-images-v2': u'versions-images',
            u'versions-v1': u'versions',
            u'versions-v2.1': u'versions',
            u'volume-api-v1-snapshots': u'snapshots',
            u'volume-api-v1-types': u'types',
            u'volume-api-v1-versions': u'versions',
            u'volume-api-v1-volumes': u'volumes',
            u'volume-api-v2-extensions': u'extensions',
            u'volume-api-v2-snapshots': u'snapshots',
            u'volume-api-v2-types': u'types',
            u'volume-api-v2-versions': u'versions',
            u'volume-api-v2-volumes': u'volumes',
            u'vpnaas-v2.0': u'vpnaas'}


VERSION_RE = re.compile('v[0-9\.]+')
WHITESPACE_RE = re.compile('[\s]+', re.MULTILINE)


class TableMixin(object):
    def visit_table(self, attrs):
        self.__table = prettytable.PrettyTable(hrules=prettytable.ALL)

    def depart_table(self):
        self.content.append('\n\n')
        self.content.append(str(self.__table))

    def depart_th(self):
        heading = self.content.pop().strip()
        self.__table.field_names.append(heading)
        self.__table.align[heading] = 'l'
        self.__table.valign[heading] = 'l'
        self.__table.max_width[heading] = 80

    def visit_tr(self, attrs):
        self.__row = []

    def visit_td(self, attrs):
        self.content_stack.append([])

    def depart_td(self):
        self.__row.append(''.join(self.content_stack.pop()).strip())

    def depart_tr(self):
        if self.__row:
            self.__table.add_row(self.__row)


class APIChapterContentHandler(xml.sax.ContentHandler, TableMixin):

    EMPHASIS = {
        'bold': '**',
        'italic': '*'
    }

    def __init__(self, filename, api_parser):
        self.filename = filename
        self.api_parser = api_parser

    def startDocument(self):
        super(APIChapterContentHandler, self).startDocument()
        self.tags = {}
        self.current_tag = None

        # general state
        self.tag_stack = []
        self.attr_stack = []
        self.content_stack = [[]]
        self.current_emphasis = None
        self.nesting = 0
        self.fill_width = 67
        self.wrapper = textwrap.TextWrapper(width=self.fill_width)

    @property
    def content(self):
        return self.content_stack[-1]

    def search_stack_for(self, tag_name):
        for tag, attrs in zip(reversed(self.tag_stack),
                              reversed(self.attr_stack)):
            if tag == tag_name:
                return attrs

    def on_top_tag_stack(self, *args):
        return self.tag_stack[-len(args):] == list(args)

    def startElement(self, name, _attrs):
        attrs = dict(_attrs)

        self.tag_stack.append(name)
        self.attr_stack.append(attrs)

        if self.on_top_tag_stack('chapter', 'section', 'title'):
            self.content_stack.append([])

        if self.on_top_tag_stack('chapter', 'title'):
            self.content_stack.append([])

        if self.on_top_tag_stack('chapter', 'section'):
            self.content_stack.append([])
            id = attrs['xml:id']
            id = SECTIONS.get(id, id)
            self.current_tag = {'name': id}
            self.api_parser.tags.append(self.current_tag)

        if name == 'wadl:resource':
            filename, resource_id = attrs['href'].split("#")
            dir = path.dirname(self.filename)
            filepath = path.abspath(path.join(dir, filename))
            self.api_parser.resource_tags[filepath + '#' + resource_id] = self.current_tag['name']

        if name == 'wadl:resources':
            if 'href' in attrs:
                dir = path.dirname(self.filename)
                filepath = path.abspath(path.join(dir, attrs['href']))
                self.api_parser.file_tags[filepath] = self.current_tag['name']

        if self.on_top_tag_stack('wadl:resource', 'wadl:method'):
            resource = self.search_stack_for('wadl:resource')
            dir = path.dirname(self.filename)
            filename = resource['href'].split("#")[0]
            filepath = path.abspath(path.join(dir, filename))
            self.api_parser.method_tags[filepath + attrs['href']] = self.current_tag['name']

        fn = getattr(self, 'visit_%s' % name, None)
        if fn:
            fn(dict(_attrs))

    def endElement(self, name):
        content = ''.join(self.content)

        if self.on_top_tag_stack('chapter', 'section', 'title'):
            self.current_tag['description'] = content.strip()
            self.content_stack.pop()

        if self.on_top_tag_stack('chapter', 'title'):
            title = content.strip()
            title = title.split('API', 1)[0]
            title = title + 'API'
            self.api_parser.title = title
            self.content_stack.pop()

        if self.on_top_tag_stack('chapter', 'section'):
            self.current_tag['summary'] = content.strip()
            self.content_stack.pop()

        self.tag_stack.pop()
        self.attr_stack.pop()

        fn = getattr(self, 'depart_%s' % name, None)
        if fn:
            fn()

    def characters(self, content):
        if not content:
            return
        # Fold up any white space into a single char
        content = WHITESPACE_RE.sub(' ', content)
        if content == ' ':
            return
        if content[0] == '\n':
            return
        if self.content:
            if self.content[-1].endswith('\n'):
                content = ' ' * self.nesting + content.strip()
            elif self.content[-1].endswith(' '):
                content = content.strip()
            elif (not self.on_top_tag_stack('emphasis')
                  and not self.on_top_tag_stack('code')):
                content = ' ' + content.strip()
            else:
                content = content.strip()

        self.content.append(content)

    def visit_listitem(self, attrs):
        self.nesting = len([tag for tag in self.tag_stack
                            if tag == 'listitem']) - 1
        self.content_stack.append([' ' * self.nesting + '-'])
        self.wrapper = textwrap.TextWrapper(
            width=self.fill_width,
            initial_indent=' ',
            subsequent_indent=' ' * self.nesting + '  ',)

    def depart_listitem(self):
        content = self.content_stack.pop()
        self.content.append(''.join(content))
        self.content.append('\n')

        self.nesting = len([tag for tag in self.tag_stack
                            if tag == 'listitem'])

    def depart_itemizedlist(self):
        if self.search_stack_for('itemizedlist') is None:
            self.wrapper = textwrap.TextWrapper(width=self.fill_width)

    def depart_orderedlist(self):
        if self.search_stack_for('itemizedlist') is None:
            self.wrapper = textwrap.TextWrapper(width=self.fill_width)

    def visit_para(self, attrs):
        self.content_stack.append([''])
        if self.search_stack_for('itemizedlist') is not None:
            return
        if self.content:
            if self.content[-1].endswith('\n\n'):
                pass
            elif self.content[-1].endswith('\n'):
                self.content.append('\n')

    def depart_para(self):
        content = ''.join(self.content_stack.pop()).strip()
        wrapped = self.wrapper.wrap(content)
        self.content.append('\n'.join(wrapped))
        if self.search_stack_for('itemizedlist') is None:
            self.content.append('\n\n')
        else:
            self.content.append('\n')
            self.wrapper = textwrap.TextWrapper(
                width=self.fill_width,
                initial_indent=' ' * self.nesting + '  ',
                subsequent_indent=' ' * self.nesting + '  ',)

    def visit_code(self, attrs):
        if not self.content[-1].endswith(' '):
            self.content.append(' ')
        self.content.append('``')

    def depart_code(self):
        self.content.append('``')

    def visit_emphasis(self, attrs):
        # Bold is the default emphasis
        self.current_emphasis = attrs.get('role', 'bold')
        if not self.content[-1].endswith(' '):
            self.content.append(' ')
        self.content.append(self.EMPHASIS[self.current_emphasis])

    def depart_emphasis(self):
        self.content.append(self.EMPHASIS[self.current_emphasis])
        self.current_emphasis = None


class APIRefContentHandler(xml.sax.ContentHandler):

    def __init__(self, filename):
        self.filename = filename

    def startDocument(self):
        self.tags = []
        self.current_tag = None
        self.method_tags = {}
        self.resource_tags = {}
        self.file_tags = {}

        # general state
        self.tag_stack = []
        self.attr_stack = []
        self.content = None

    def search_stack_for(self, tag_name):
        for tag, attrs in zip(reversed(self.tag_stack),
                              reversed(self.attr_stack)):
            if tag == tag_name:
                return attrs

    def on_top_tag_stack(self, *args):
        return self.tag_stack[-len(args):] == list(args)

    def startElement(self, name, _attrs):
        attrs = dict(_attrs)
        self.tag_stack.append(name)
        self.attr_stack.append(attrs)
        self.content = []
        if self.on_top_tag_stack('book'):
            id = attrs['xml:id']
            extensions = False
            if id.endswith('-ext'):
                extensions = True
                id = id.rsplit('-', 1)[0]
            service, version = id.rsplit('-', 1)
            if service.startswith('api.openstack.org-'):
                service = service.split('-', 1)[1]
            if extensions:
                service = service + '-extensions'
            assert VERSION_RE.match(version)
            self.service = service
            self.version = version
        if self.on_top_tag_stack('book', 'xi:include'):
            filename = attrs['href']
            dir = path.dirname(self.filename)
            filepath = path.join(dir, filename)
            ch = APIChapterContentHandler(filepath, self)
            xml.sax.parse(filepath, ch)

    def endElement(self, name):
        self.tag_stack.pop()
        self.attr_stack.pop()

    def characters(self, content):
        content = content.strip()
        if content:
            self.content.append(content)


def main(source_file, output_dir):
    log.info('Parsing %s' % source_file)
    ch = APIRefContentHandler(source_file)
    xml.sax.parse(source_file, ch)
    os.chdir(output_dir)
    output = {
        'title': ch.title,
        'service': ch.service,
        'version': ch.version,
        'tags': ch.tags,
        'method_tags': ch.method_tags,
        'file_tags': ch.file_tags,
        'resource_tags': ch.resource_tags,
    }
    pathname = 'api-ref-%s-%s.json' % (ch.service,
                                       ch.version)
    with open(pathname, 'w') as out_file:
        json.dump(output, out_file, indent=2, sort_keys=True)


if '__main__' == __name__:
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help="Increase verbosity (specify multiple times for more)")
    parser.add_argument(
        '-o', '--output-dir', action='store',
        help="The directory to output the JSON files too.")
    parser.add_argument(
        'filename',
        help="File to convert")

    args = parser.parse_args()

    log_level = logging.WARNING
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s %(name)s %(levelname)s %(message)s')

    filename = path.abspath(args.filename)

    main(filename, output_dir=args.output_dir)
