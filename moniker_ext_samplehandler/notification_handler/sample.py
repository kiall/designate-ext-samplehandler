# Copyright 2013 Hewlett-Packard Development Company, L.P.
#
# Author: Kiall Mac Innes <kiall@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from moniker.openstack.common import cfg
from moniker.openstack.common import log as logging
from moniker.notification_handler.base import Handler

LOG = logging.getLogger(__name__)

# Setup a config group
#cfg.CONF.register_group(cfg.OptGroup(
#    name='handler:sample',
#    title="Configuration for Sample Notification Handler"
#))

# Setup the config options
#cfg.CONF.register_opts([
#    cfg.StrOpt('format', default=None)
#], group='handler:sample')


class SampleHandler(Handler):
    """ Sample Handler """
    __plugin_name__ = 'sample'

    def process_notification(self, event_type, payload):
        # Do something with the notification.. e.g:
        domain_id = '12345'
        
        self.central_api.create_record(domain_id, name='my-server.domain.com.',
                                       type='A', data='127.0.0.1')
