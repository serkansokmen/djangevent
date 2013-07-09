'use strict';

eventsApp.controller('EventListController', function EventListController ($scope, $location, eventsData) {
    $scope.events = eventsData.getAllEvents();
});
