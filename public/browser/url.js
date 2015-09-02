(function (root, factory) {
    if (typeof exports === 'object') {
        module.exports = factory();
    } else if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else {
        root.urldescription = factory();
    }
}(this, function () {
  function UrlDescription() {
  }

  UrlDescription.prototype.parse = function (template) {
    var that = this;

    return {
      annotate: function (context) {
        var context_map = {};
        angular.forEach(context, function(value) {
          context_map[value.name] = value;
        });

        return template.replace(/\{([^\{\}]+)\}|([^\{\}]+)/g, function (_, key, literal) {
          if (key) {
            var value = context_map[key];
            if (value !== undefined && value !== null) {
              return '<abbr title="' + value.description + '">{' + value.name + '}</abbr>';
            } else {
              return '{' + key + '}';
            }
          } else {
            return literal;
          }
        });
      }
    };
  };

  return new UrlDescription();
}));
