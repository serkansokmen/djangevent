"use strict";

eventsApp.factory('eventsData', function ($q, $resource) {
    var resource = $resource('/api/events/:id', {id: '@id'});

    return {
        getEvent: function (id) {
            var deferred = $q.defer();
            resource.get({id: id},
                function (event) { deferred.resolve(event); },
                function (response) { deferred.reject(response);}
            );
            return deferred.promise;
        },
        save: function (event) {
            var deferred = $q.defer();
            event.id = 999;
            resource.save(event,
                function (response) { deferred.resolve(response); },
                function (response) { deferred.reject(response); }
            );
            return deferred.promise;
        },
        getAllEvents: function () {
            return resource.query();
        }
    };
});
