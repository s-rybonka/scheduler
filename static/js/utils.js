var DEFAULT_DATE_TIME_FORMAT = 'YYYY-MM-DD HH:mm';

function setCookie(key, value, expiry) {
  var expires = new Date();
  expires.setTime(expires.getTime() + (expiry * 24 * 60 * 60 * 1000));
  document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function eraseCookie(key) {
  var keyValue = getCookie(key);
  setCookie(key, keyValue, '-1');
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});

function getFormattedFormData($form) {
  var unindexed_array = $form.serializeArray();
  var indexed_array = {};
  $.map(unindexed_array, function (n, i) {
    indexed_array[n['name']] = n['value'];
  });
  return indexed_array;
}

var BUTTONS = {
  add: "<button type='button' class='btn btn-primary create-btn'>Add</button>",
  update: "<button type='button' class='btn btn-primary update-btn'>Update</button>",
  delete: "<button type='button' class='btn btn-warning delete-btn'>Delete</button>",
  close: "<button type='button' class='btn btn-danger close-btn' data-dismiss='modal'>Close</button>",
};

function getFormInputIds(form_name) {
  var $inputs = $(`#${form_name} :input`);
  var form_input_ids = [];
  $inputs.each(function () {
    form_input_ids.push(`#${this.id}`)
  });
  return form_input_ids
}

function processDataForMethod($form, method, instance) {
  var formatted_form_data = getFormattedFormData(
    $form
  );
  handlers = {
    POST: function () {
      return formatted_form_data
    },
    PATCH: function () {
      if (instance) {
        var old_start_date_time = moment(instance['start']).format(
          DEFAULT_DATE_TIME_FORMAT
        );
        var old_end_date_time = moment(instance['end']).format(
          DEFAULT_DATE_TIME_FORMAT
        );
        
        $.each(formatted_form_data, function (key, value) {
          if (instance[key] === value) {
            delete formatted_form_data[key]
          } else if (old_start_date_time === value && !instance.has_drop_event) {
            delete formatted_form_data[key]
          } else if (old_end_date_time === value && !instance.has_drop_event) {
            delete formatted_form_data[key]
          } else if (instance['extendedProps'][key] === value) {
            delete formatted_form_data[key]
          }
        });
      }
      return formatted_form_data
    },
    DELETE: function () {
      return {}
    }
  };
  return JSON.stringify(handlers[method]())
}