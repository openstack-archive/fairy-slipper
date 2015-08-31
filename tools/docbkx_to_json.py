#!/usr/bin/env python
# Copyright (c) 2015 Russell Sim <russell.sim@gmail.com>
#
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


SECTIONS = {'API_Versions': 'api-versions',
            'Database_Instances': 'database-instances',
            'admin-tenants': 'admin-tenants',
            'admin-tokens': 'admin-tokens',
            'admin-users': 'admin-users',
            'admin-versions': 'admin-versions',
            'alarms': 'alarms',
            'build-info': 'build-info',
            'capabilities': 'capabilities',
            'compute_extensions': 'extensions',
            'compute_flavors': 'flavors',
            'compute_image_metadata': 'image-metadata',
            'compute_images': 'images',
            'compute_limits': 'limits',
            'compute_server-actions': 'server-actions',
            'compute_server-addresses': 'server-addresses',
            'compute_server_metadata': 'server-metadata',
            'compute_servers': 'servers',
            'compute_versions': 'versions',
            'credentials-v3': 'credentials',
            'database-instance-actions': 'database-instance-actions',
            'databases': 'databases',
            'datastores': 'datastores',
            'diagnostics-v2.1': 'diagnostics',
            'domains-v3': 'domains',
            'endpoints-v3': 'endpoints',
            'ext-backups-v2': 'ext-backups',
            'extraroute-ext': 'extraroute',
            'flavor-extra-specs-v2.1': 'flavor-extra-specs',
            'flavors': 'flavors',
            'general-info': 'general-info',
            'groups-v3': 'groups',
            'heat-versions': 'heat-versions',
            'identity-auth-v2': 'identity-auth',
            'identity-v2-versions': 'versions',
            'identity_v3_OS-INHERIT-ext': 'inherit',
            'identity_v3_OS-KDS-ext': 'kds',
            'identity_v3_OS-OAUTH1-ext': 'oauth1',
            'identity_v3_OS-TRUST-ext': 'trust',
            'image-data-v2': 'image-data',
            'image-schemas-v2': 'image-schemas',
            'image-tags-v2': 'image-tags',
            'images-v1': 'images',
            'images-v2': 'images',
            'keypairs-v2.1': 'keypairs',
            'layer3': 'layer3',
            'lbaas-v1.0': 'lbaas',
            'lbaas-v2.0': 'lbaas',
            'limits-v2.1': 'limits',
            'members-v1': 'members',
            'members-v2': 'members',
            'metering-ext': 'metering',
            'meters': 'meters',
            'network_multi_provider-ext': 'network-multi-provider',
            'network_provider-ext': 'network-provider',
            'network_vlan_transparency-ext': 'network-vlan-transparency',
            'networks': 'networks',
            'neutron-versions-v2': 'versions',
            'neutron_extensions': 'extensions',
            'os-admin-actions': 'admin-actions',
            'os-admin-actions-v2.1': 'admin-actions',
            'os-admin-password-v2.1': 'admin-password',
            'os-agents': 'agents',
            'os-agents-v2.1': 'agents',
            'os-aggregates': 'aggregates',
            'os-aggregates-v2.1': 'aggregates',
            'os-availability-zone': 'availability-zone',
            'os-availability-zone-v2.1': 'availability-zone',
            'os-baremetal-ext-status': 'baremetal-ext-status',
            'os-block-device-mapping-v2-boot': 'block-device-mapping',
            'os-cells-v2.1': 'cells',
            'os-certificates': 'certificates',
            'os-certificates-v2.1': 'certificates',
            'os-cloudpipe': 'cloudpipe',
            'os-config-drive-v2.1': 'config-drive',
            'os-console-output': 'console-output',
            'os-console-output-v2.1': 'console-output',
            'os-consoles': 'consoles',
            'os-coverage': 'coverage',
            'os-create-backup-v2.1': 'create-backup',
            'os-createserverext': 'createserverext',
            'os-deferred-delete': 'deferred-delete',
            'os-deferred-delete-v2.1': 'deferred-delete',
            'os-diagnostics': 'diagnostics',
            'os-disk-config': 'disk-config',
            'os-evacuate-v2.1': 'evacuate',
            'os-ext-az': 'ext-az',
            'os-ext-img-size': 'ext-img-size',
            'os-ext-ips': 'ext-ips',
            'os-extended-availability-zone-v2.1': 'extended-availability-zone',
            'os-extended-networks': 'extended-networks',
            'os-extended-server-attributes': 'extended-server-attributes',
            'os-extended-server-attributes-v2.1': 'extended-server-attributes',
            'os-extended-status': 'extended-status',
            'os-extended-status-v2.1': 'extended-status',
            'os-fixed-ips': 'fixed-ips',
            'os-flavor-access': 'flavor-access',
            'os-flavor-access-v2.1': 'flavor-access',
            'os-flavor-extra-specs': 'flavor-extra-specs',
            'os-flavor-manage-v2.1': 'flavor-manage',
            'os-flavor-rxtx': 'flavor-rxtx',
            'os-flavor-rxtx-v2.1': 'flavor-rxtx',
            'os-flavor-swap': 'flavor-swap',
            'os-flavorextradata': 'flavorextradata',
            'os-flavormanage': 'flavormanage',
            'os-flavors-v2.1': 'flavors',
            'os-floating-ip-dns': 'floating-ip-dns',
            'os-floating-ip-dns-v2.1': 'floating-ip-dns',
            'os-floating-ip-pools': 'floating-ip-pools',
            'os-floating-ip-pools-v2.1': 'floating-ip-pools',
            'os-floating-ips': 'floating-ips',
            'os-floating-ips-bulk': 'floating-ips-bulk',
            'os-floating-ips-bulk-v2.1': 'floating-ips-bulk',
            'os-floating-ips-v2.1': 'floating-ips',
            'os-flv-disabled': 'flv-disabled',
            'os-hosts': 'hosts',
            'os-hosts-v2.1': 'hosts',
            'os-hypervisor-status': 'hypervisor-status',
            'os-hypervisors': 'hypervisors',
            'os-hypervisors-v2.1': 'hypervisors',
            'os-instance-actions': 'instance-actions',
            'os-instance-actions-v2.1': 'instance-actions',
            'os-instance-usage-audit-log-v2.1': 'instance-usage-audit-log',
            'os-interface': 'interface',
            'os-keypairs': 'keypairs',
            'os-ksadm-admin-ext': 'ksadm-admin',
            'os-kscatalog-ext': 'kscatalog',
            'os-ksec2-admin-ext': 'ksec2-admin',
            'os-kss3-admin-ext': 'kss3-admin',
            'os-ksvalidate-ext': 'ksvalidate',
            'os-limits-v2': 'limits',
            'os-metadef-namespace-v2': 'metadef-namespace',
            'os-metadef-object-v2': 'metadef-object',
            'os-metadef-property-v2.wadl': 'metadef-property',
            'os-metadef-resourcetype-v2': 'metadef-resourcetype',
            'os-metadef-schemas-v2': 'metadef-schemas',
            'os-metadef-tag-v2': 'metadef-tag',
            'os-migrations': 'migrations',
            'os-migrations-v2.1': 'migrations',
            'os-multi-server-create': 'multi-server-create',
            'os-multinic-v2.1': 'multinic',
            'os-multiple-create-v2.1': 'multiple-create',
            'os-networks': 'networks',
            'os-networks-v2.1': 'networks',
            'os-qos-v2-qos-specs': 'qos-v2-qos-specs',
            'os-quota-class-sets': 'quota-class-sets',
            'os-quota-class-sets-v2.1': 'quota-class-sets',
            'os-quota-sets': 'quota-sets',
            'os-quota-sets-v2': 'quota-sets',
            'os-quota-sets-v2.1': 'quota-sets',
            'os-remote-consoles-v2.1': 'remote-consoles',
            'os-rescue': 'rescue',
            'os-scheduler-hints': 'scheduler-hints',
            'os-security-group-default-rules': 'security-group-default-rules',
            'os-security-groups': 'security-groups',
            'os-security-groups-v2.1': 'security-groups',
            'os-server-OS-EXT-IPS-MAC': 'server-ext-ips-mac',
            'os-server-actions-v2.1': 'server-actions',
            'os-server-groups': 'server-groups',
            'os-server-groups-v2.1': 'server-groups',
            'os-server-password': 'server-password',
            'os-server-password-v2.1': 'server-password',
            'os-server-shelve': 'server-shelve',
            'os-server-start-stop': 'server-start-stop',
            'os-server-usage-v2.1': 'server-usage',
            'os-services': 'services',
            'os-services-v2.1': 'services',
            'os-shelve-v2.1': 'shelve',
            'os-simple-tenant-usage': 'simple-tenant-usage',
            'os-tenant-networks-v2.1': 'tenant-networks',
            'os-used-limits': 'used-limits',
            'os-used-limits-for-admins': 'used-limits-for-admins',
            'os-virtual-interfaces': 'virtual-interfaces',
            'os-virtual-interfaces-v2.1': 'virtual-interfaces',
            'os-volume': 'volume',
            'os-volume-manage-v2': 'volume-manage',
            'os-volume-type-access-v2': 'volume-type-access',
            'os-volume_attachments': 'volume-attachments',
            'policies-v3': 'policies',
            'port_binding-ext': 'port-binding',
            'ports': 'ports',
            'projects-v3': 'projects',
            'quotas-ext': 'quotas',
            'resources': 'resources',
            'roles-v3': 'roles',
            'samples': 'samples',
            'security_groups': 'security-groups',
            'server-ips-v2.1': 'server-ips',
            'service-catalog-v3': 'service-catalog',
            'service-status': 'service-status',
            'shared_images_v1': 'shared-images',
            'software-config': 'software-config',
            'stack-actions': 'stack-actions',
            'stack-events': 'stack-events',
            'stack-resources': 'stack-resources',
            'stack-templates': 'stack-templates',
            'stacks': 'stacks',
            'storage_account_services': 'storage-account-services',
            'storage_container_services': 'storage-container-services',
            'storage_object_services': 'storage-object-services',
            'subnets': 'subnets',
            'tokens-v3': 'tokens',
            'user_management': 'user-management',
            'users-v3': 'users',
            'v1.1clusters': 'clusters',
            'v1.1clustertemplate': 'clustertemplate',
            'v1.1datasources': 'datasources',
            'v1.1event-log': 'event-log',
            'v1.1imageregistry': 'imageregistry',
            'v1.1jobbinaries': 'jobbinaries',
            'v1.1jobbinary-internals': 'jobbinary-internals',
            'v1.1jobexecutions': 'job-executions',
            'v1.1jobs': 'jobs',
            'v1.1jobtypes': 'job-types',
            'v1.1nodegrouptemplate': 'node-group-template',
            'v1.1plugins': 'plugins',
            'v2.1os-fping': 'fping',
            'versions-identity-v3': 'versions-identity',
            'versions-images-v2': 'versions-images',
            'versions-v1': 'versions',
            'versions-v2.1': 'versions',
            'volume-api-v1-snapshots': 'snapshots',
            'volume-api-v1-types': 'types',
            'volume-api-v1-versions': 'versions',
            'volume-api-v1-volumes': 'volumes',
            'volume-api-v2-extensions': 'extensions',
            'volume-api-v2-snapshots': 'snapshots',
            'volume-api-v2-types': 'types',
            'volume-api-v2-versions': 'versions',
            'volume-api-v2-volumes': 'volumes',
            'vpnaas-v2.0': 'vpnaas'}


VERSION_RE = re.compile('v[0-9\.]+')
WHITESPACE_RE = re.compile('[\s]+', re.MULTILINE)
TITLE_RE = re.compile(
    '(.*) API v([\d.]+) (\S*)[ ]*\((SUPPORTED|CURRENT|DEPRECATED)\)')


class TableMixin(object):
    def visit_table(self, attrs):
        self.__table = prettytable.PrettyTable(hrules=prettytable.ALL)

    def depart_table(self):
        self.content.append('\n\n')
        self.content.append(str(self.__table))
        self.content.append('\n\n')

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
        self.no_space = False
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
            match = TITLE_RE.match(title)
            if match:
                title, version, ext, state = match.groups()
            else:
                raise Exception("Title %s doesn't match RE" % title)
            self.api_parser.title = ('%s %s' % (title, ext)).strip()
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
        if not self.on_top_tag_stack('programlisting'):
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
            elif (self.on_top_tag_stack('programlisting')):
                content = ' ' * self.nesting + content
            elif self.no_space:
                content = content.strip()
                self.no_space = False
            else:
                content = '' + content.strip()

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
        self.no_space = True

    def depart_code(self):
        self.content.append('``')
        if not self.content[-1].endswith(' '):
            self.content.append(' ')
        
    def visit_emphasis(self, attrs):
        # Bold is the default emphasis
        self.current_emphasis = attrs.get('role', 'bold')
        if not self.content[-1].endswith(' '):
            self.content.append(' ')
        self.content.append(self.EMPHASIS[self.current_emphasis])
        self.no_space = True

    def depart_emphasis(self):
        self.content.append(self.EMPHASIS[self.current_emphasis])
        self.current_emphasis = None

    def visit_programlisting(self, attrs):
        if not attrs:
            self.content.append('::\n')
        else:
            self.content.append('.. code-block:: %s\n' % attrs['language'])
        self.nesting = 3

    def depart_programlisting(self):
        self.content.append('\n')
        self.nesting = 0


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
