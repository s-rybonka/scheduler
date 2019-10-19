$(document).ready(function () {
  
  var $document = $(document);
  var $event_modal = $("#event-modal");
  var $modal_action_buttons = $('.action-buttons');
  var $modal_heading = $('.heading');
  var $event_form_component = $("#event-form-component");
  var calendarEl = document.getElementById('calendar');
  var event_list_url = JSON.parse($('#event_list_id').text());
  var DEFAULT_DATE_TIME_FORMAT = 'YYYY-MM-DD hh:mm';
  
  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: ['dayGrid', 'interaction'],
    selectable: true,
    selectHelper: true,
    editable: true,
    eventLimit: true,
    height: 800,
    titleFormat: {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    },
    events: function (info, successCallback, failureCallback) {
      $.ajax({
        type: 'GET',
        url: event_list_url,
        success: function (response) {
          successCallback(response.map(function (event) {
              return {
                id: event.id,
                title: event.title,
                start: event.start_date_time,
                end: event.end_date_time,
                extendedProps: {
                  description: event.description,
                  absolute_uri: event.abs_uri,
                },
              }
            })
          );
        },
        error: function (response) {
          failureCallback(response);
        },
      });
    },
    dateClick: function (info) {
      initEventFrom('create')
    },
    eventClick: function (data) {
      initEventFrom('update', data.event);
    },
  });
  
  function initEventFrom(action_type, event) {
    var EVENT_FORM_ATTRS = {
      title: 'Title:',
      description: 'Description:',
      start_date_time: 'Start at:',
      end_date_time: 'End at:',
    };
    
    $.each(EVENT_FORM_ATTRS, function (key, value) {
      $(`.label-dyn-${key}`).html(value)
    });
    
    if (action_type === 'update' && event) {
      var initial_values = getFormattedEventData(event);
      var event_id = initial_values.id;
      var event_abs_url = initial_values.abs_uri;
      
      delete initial_values.id;
      delete initial_values.abs_uri;
      
      $event_form_component.attr('action', event_abs_url);
      $event_form_component.attr('data-event-id', event_id);
      
      $.each(initial_values, function (key, value) {
        $(`#${key}_id`).val(value)
      });
    } else if (action_type === 'create' && !event) {
      $event_form_component.attr('action', event_list_url);
      $event_form_component[0].reset()
    }
    setModalContextData(action_type);
  }
  
  function setModalContextData(action_type) {
    var EVENT_MODAL_ATTRS = {
      heading: {
        create: 'Add new Event',
        update: 'Update Event'
      },
      action_buttons: {
        create: {
          close: BUTTONS.close,
          add: BUTTONS.add,
        },
        update: {
          close: BUTTONS.close,
          delete: BUTTONS.delete,
          update: BUTTONS.update,
        }
      },
    };
    
    $modal_heading.html(EVENT_MODAL_ATTRS.heading[action_type]);
    
    if ($modal_action_buttons.children().length) {
      $modal_action_buttons.empty()
    }
    $.each(EVENT_MODAL_ATTRS.action_buttons[action_type], function (key, value) {
      $modal_action_buttons.append(value)
    });
    
    $event_modal.modal('show')
  }
  
  function getFormattedEventData(raw_event_data) {
    return {
      id: raw_event_data.id,
      title: raw_event_data.title,
      description: raw_event_data.extendedProps.description,
      start_date_time: moment(raw_event_data.start).format(DEFAULT_DATE_TIME_FORMAT),
      end_date_time: moment(raw_event_data.end).format(DEFAULT_DATE_TIME_FORMAT),
      abs_uri: raw_event_data.extendedProps.absolute_uri,
    };
  }
  
  function makeApiCall(jq_event) {
    var data = jq_event.data;
    $.ajax({
      type: data.method,
      url: data.form.attr('action'),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      data: JSON.stringify(
        getFormData(data.form)
      ),
      success: function (response) {
        data.successHandler(response)
      },
      error: function (response) {
        data.errorHandler(response)
      },
    });
  }
  
  function createEventHandler(data) {
    calendar.addEvent({
      title: data.title,
      description: data.description,
      start: data.start_date_time,
      end: data.end_date_time,
    });
    $event_modal.modal('hide');
  }
  
  function updateEventHandler(data) {
    var event = calendar.getEventById(data.id);
    event.setProp('title', data.title);
    event.setProp('description', data.description);
    event.setDates(
      data.start_date_time,
      data.end_date_time
    );
    $event_modal.modal('hide');
  }
  
  function deleteEventHandler(data) {
    var event = calendar.getEventById($event_form_component.attr('data-event-id'));
    event.remove();
    $event_modal.modal('hide');
  }
  
  function eventActionErrorHandler(data) {
    var errors = data.responseJSON;
    $.map(errors, function (value, key) {
      $(`.${key}-error`).html(value)
    });
  }
  
  function bindEventHandlers() {
    $document.on(
      'click', '.create-btn',
      {
        method: 'POST',
        form: $event_form_component,
        successHandler: createEventHandler,
        errorHandler: eventActionErrorHandler
      },
      makeApiCall,
    );
    
    $document.on(
      'click', '.update-btn',
      {
        method: 'PATCH',
        form: $event_form_component,
        successHandler: updateEventHandler,
        errorHandler: eventActionErrorHandler
      },
      makeApiCall,
    );
    
    $document.on(
      'click', '.delete-btn',
      {
        method: 'DELETE',
        form: $event_form_component,
        successHandler: deleteEventHandler,
        errorHandler: eventActionErrorHandler
      },
      makeApiCall,
    );
  }
  
  calendar.render();
  bindEventHandlers();
  
});
