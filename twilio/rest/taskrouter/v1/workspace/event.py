# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class EventList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the EventList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: The sid
        
        :returns: EventList
        :rtype: EventList
        """
        super(EventList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Events'.format(**self._kwargs)

    def stream(self, end_date=values.unset, event_type=values.unset,
               minutes=values.unset, reservation_sid=values.unset,
               start_date=values.unset, task_queue_sid=values.unset,
               task_sid=values.unset, worker_sid=values.unset,
               workflow_sid=values.unset, limit=None, page_size=None, **kwargs):
        """
        Streams EventInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param datetime end_date: The end_date
        :param str event_type: The event_type
        :param str minutes: The minutes
        :param str reservation_sid: The reservation_sid
        :param datetime start_date: The start_date
        :param str task_queue_sid: The task_queue_sid
        :param str task_sid: The task_sid
        :param str worker_sid: The worker_sid
        :param str workflow_sid: The workflow_sid
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'EndDate': serialize.iso8601_datetime(end_date),
            'EventType': event_type,
            'Minutes': minutes,
            'ReservationSid': reservation_sid,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskQueueSid': task_queue_sid,
            'TaskSid': task_sid,
            'WorkerSid': worker_sid,
            'WorkflowSid': workflow_sid,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            EventInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, end_date=values.unset, event_type=values.unset,
             minutes=values.unset, reservation_sid=values.unset,
             start_date=values.unset, task_queue_sid=values.unset,
             task_sid=values.unset, worker_sid=values.unset,
             workflow_sid=values.unset, limit=None, page_size=None, **kwargs):
        """
        Reads EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param datetime end_date: The end_date
        :param str event_type: The event_type
        :param str minutes: The minutes
        :param str reservation_sid: The reservation_sid
        :param datetime start_date: The start_date
        :param str task_queue_sid: The task_queue_sid
        :param str task_sid: The task_sid
        :param str worker_sid: The worker_sid
        :param str workflow_sid: The workflow_sid
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            end_date=end_date,
            event_type=event_type,
            minutes=minutes,
            reservation_sid=reservation_sid,
            start_date=start_date,
            task_queue_sid=task_queue_sid,
            task_sid=task_sid,
            worker_sid=worker_sid,
            workflow_sid=workflow_sid,
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, end_date=values.unset, event_type=values.unset,
             minutes=values.unset, reservation_sid=values.unset,
             start_date=values.unset, task_queue_sid=values.unset,
             task_sid=values.unset, worker_sid=values.unset,
             workflow_sid=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        """
        Retrieve a single page of EventInstance records from the API.
        Request is executed immediately
        
        :param datetime end_date: The end_date
        :param str event_type: The event_type
        :param str minutes: The minutes
        :param str reservation_sid: The reservation_sid
        :param datetime start_date: The start_date
        :param str task_queue_sid: The task_queue_sid
        :param str task_sid: The task_sid
        :param str worker_sid: The worker_sid
        :param str workflow_sid: The workflow_sid
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of EventInstance
        :rtype: Page
        """
        params = values.of({
            'EndDate': serialize.iso8601_datetime(end_date),
            'EventType': event_type,
            'Minutes': minutes,
            'ReservationSid': reservation_sid,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskQueueSid': task_queue_sid,
            'TaskSid': task_sid,
            'WorkerSid': worker_sid,
            'WorkflowSid': workflow_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            EventInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def get(self, sid):
        """
        Constructs a EventContext
        
        :param sid: The sid
        
        :returns: EventContext
        :rtype: EventContext
        """
        return EventContext(self._version, sid=sid, **self._kwargs)

    def __call__(self, sid):
        """
        Constructs a EventContext
        
        :param sid: The sid
        
        :returns: EventContext
        :rtype: EventContext
        """
        return EventContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.EventList>'


class EventContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the EventContext
        
        :param Version version
        :param workspace_sid: The workspace_sid
        :param sid: The sid
        
        :returns: EventContext
        :rtype: EventContext
        """
        super(EventContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Events/{sid}'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a EventInstance
        
        :returns: Fetched EventInstance
        :rtype: EventInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            EventInstance,
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
        return '<Twilio.Taskrouter.V1.EventContext {}>'.format(context)


class EventInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        """
        Initialize the EventInstance
        
        :returns: EventInstance
        :rtype: EventInstance
        """
        super(EventInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'actor_sid': payload['actor_sid'],
            'actor_type': payload['actor_type'],
            'actor_url': payload['actor_url'],
            'description': payload['description'],
            'event_data': payload['event_data'],
            'event_date': deserialize.iso8601_datetime(payload['event_date']),
            'event_type': payload['event_type'],
            'resource_sid': payload['resource_sid'],
            'resource_type': payload['resource_type'],
            'resource_url': payload['resource_url'],
            'sid': payload['sid'],
            'source': payload['source'],
            'source_ip_address': payload['source_ip_address'],
            'url': payload['url'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: EventContext for this EventInstance
        :rtype: EventContext
        """
        if self._instance_context is None:
            self._instance_context = EventContext(
                self._version,
                self._kwargs['workspace_sid'],
                self._kwargs['sid'],
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
    def actor_sid(self):
        """
        :returns: The actor_sid
        :rtype: str
        """
        return self._properties['actor_sid']

    @property
    def actor_type(self):
        """
        :returns: The actor_type
        :rtype: str
        """
        return self._properties['actor_type']

    @property
    def actor_url(self):
        """
        :returns: The actor_url
        :rtype: str
        """
        return self._properties['actor_url']

    @property
    def description(self):
        """
        :returns: The description
        :rtype: str
        """
        return self._properties['description']

    @property
    def event_data(self):
        """
        :returns: The event_data
        :rtype: str
        """
        return self._properties['event_data']

    @property
    def event_date(self):
        """
        :returns: The event_date
        :rtype: datetime
        """
        return self._properties['event_date']

    @property
    def event_type(self):
        """
        :returns: The event_type
        :rtype: str
        """
        return self._properties['event_type']

    @property
    def resource_sid(self):
        """
        :returns: The resource_sid
        :rtype: str
        """
        return self._properties['resource_sid']

    @property
    def resource_type(self):
        """
        :returns: The resource_type
        :rtype: str
        """
        return self._properties['resource_type']

    @property
    def resource_url(self):
        """
        :returns: The resource_url
        :rtype: str
        """
        return self._properties['resource_url']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def source(self):
        """
        :returns: The source
        :rtype: str
        """
        return self._properties['source']

    @property
    def source_ip_address(self):
        """
        :returns: The source_ip_address
        :rtype: str
        """
        return self._properties['source_ip_address']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a EventInstance
        
        :returns: Fetched EventInstance
        :rtype: EventInstance
        """
        return self._context.fetch()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.EventInstance {}>'.format(context)
