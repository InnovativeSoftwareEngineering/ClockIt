(function () {
    "use strict";

    function add_event(start, end, jsEvent, view) {
        var event = {
            title: 'test',
            start: start,
            end: end
        };

        return $.ajax({
            type: "POST",
            url: "/event/add",
            data: event,
            dataType: "json",
            success: function () {

            }
        });
    }

    function click_event(event, jsEvent, view) {
        $.ajax({
            type: "POST",
            url: "/event/edit/" + event.id,
            data: event,
            dataType: "json",
            success: function () {

            }
        });
    }

    function drop_event(event, delta, revertFunc, jsEvent, ui, view) {
        $.ajax({
            type: "POST",
            url: "/event/edit/" + event.id,
            data: event,
            dataType: "json",
            success: function () {

            }
        });
    }

    function resize_event(event, delta, revertFunc, jsEvent, ui, view) {
        $.ajax({
            type: "POST",
            url: "/event/edit/" + event.id,
            data: event,
            dataType: "json",
            success: function () {

            }
        });
    }

    function delete_event(event) {
        $.ajax({
            type: "POST",
            url: "/event/delete/" + event.id,
            dataType: "json",
            success: function () {

            }
        });
    }

    $(document).ready(function () {
        $("#calendar").fullCalendar({
            defaultView: "agendaDay",
            editable: true,
            eventClick: click_event,
            eventDrop: drop_event,
            eventResize: resize_event,
            eventSources: [
                {
                    url: "/events_feed",
                    cache: true
                }
            ],
            header: {
                left: "today prev,next title",
                right: "month, agendaWeek, agendaDay, list"
            },
            selectable: true,
            selectHelper: true,
            select: add_event,
            titleFormat: {
                month: "MMMM YYYY",
                week: "MMM D YYYY",
                day: "ddd, MMM D, YYYY"
            }
        });
    });
}());