# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class WorkersStatisticsList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersStatisticsList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        
        :returns: WorkersStatisticsList
        :rtype: WorkersStatisticsList
        """
        super(WorkersStatisticsList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }

    def get(self):
        """
        Constructs a WorkersStatisticsContext
        
        :returns: WorkersStatisticsContext
        :rtype: WorkersStatisticsContext
        """
        return WorkersStatisticsContext(self._version, **self._kwargs)

    def __call__(self):
        """
        Constructs a WorkersStatisticsContext
        
        :returns: WorkersStatisticsContext
        :rtype: WorkersStatisticsContext
        """
        return WorkersStatisticsContext(self._version, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersStatisticsList>'


class WorkersStatisticsContext(InstanceContext):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersStatisticsContext
        
        :param Version version
        :param workspace_sid: The workspace_sid
        
        :returns: WorkersStatisticsContext
        :rtype: WorkersStatisticsContext
        """
        super(WorkersStatisticsContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workers/Statistics'.format(**self._kwargs)

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset):
        """
        Fetch a WorkersStatisticsInstance
        
        :param str minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date
        :param str task_queue_sid: The task_queue_sid
        :param str task_queue_name: The task_queue_name
        :param str friendly_name: The friendly_name
        
        :returns: Fetched WorkersStatisticsInstance
        :rtype: WorkersStatisticsInstance
        """
        params = values.of({
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
            'TaskQueueSid': task_queue_sid,
            'TaskQueueName': task_queue_name,
            'FriendlyName': friendly_name,
        })
        
        return self._version.fetch(
            WorkersStatisticsInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.WorkersStatisticsContext {}>'.format(context)


class WorkersStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid):
        """
        Initialize the WorkersStatisticsInstance
        
        :returns: WorkersStatisticsInstance
        :rtype: WorkersStatisticsInstance
        """
        super(WorkersStatisticsInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'realtime': payload['realtime'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: WorkersStatisticsContext for this WorkersStatisticsInstance
        :rtype: WorkersStatisticsContext
        """
        if self._instance_context is None:
            self._instance_context = WorkersStatisticsContext(
                self._version,
                self._kwargs['workspace_sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """
        :returns: The cumulative
        :rtype: str
        """
        return self._properties['cumulative']

    @property
    def realtime(self):
        """
        :returns: The realtime
        :rtype: str
        """
        return self._properties['realtime']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: str
        """
        return self._properties['workspace_sid']

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset):
        """
        Fetch a WorkersStatisticsInstance
        
        :param str minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date
        :param str task_queue_sid: The task_queue_sid
        :param str task_queue_name: The task_queue_name
        :param str friendly_name: The friendly_name
        
        :returns: Fetched WorkersStatisticsInstance
        :rtype: WorkersStatisticsInstance
        """
        return self._context.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            friendly_name=friendly_name,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.WorkersStatisticsInstance {}>'.format(context)
