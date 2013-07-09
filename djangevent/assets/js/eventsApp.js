'use strict';

var eventsApp = angular.module('EventsApp', ['ngResource'])
    .config(function ($interpolateProvider, $routeProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');

        $routeProvider
            .when('/events', {
                templateUrl: 'static/partials/EventList.html',
                controller: 'EventListController'
            })
            .when('/events/:eventId', {
                templateUrl: 'static/partials/EventDetail.html',
                controller: 'EventDetailController'
            })
            .when('/events/new', {
                templateUrl: 'static/partials/EventForm.html',
                controller: 'EventFormController'
            })
            .otherwise({
                redirectTo: '/events'
            });
    });
