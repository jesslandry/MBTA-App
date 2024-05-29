<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MBTA Train Schedule</title>
</head>
<body>
    <h2>Get My Train Schedule</h2>
    <form id="schedule-form" method="POST" action="/get_schedule">
        <input type="hidden" id="direction-input" name="direction">
        <button id="outbound-btn" onclick="setDirection('outbound')"> Work :( </button>
        <button id="inbound-btn" onclick="setDirection('inbound')"> Home :) </button>
    </div>

    <div id="schedule-results">
        <h3> Next Trains Scheduled For {{ destination }} </h3>
        <ul>
            {% for entry in schedule %}
            <li> {{ entry }} minutes away</li>
            {% endfor %}
        </ul>
    </div>
    
    <script>
        function setDirection(direction) {
            document.getElementById('direction-input').value = direction;
        }
    </script>
</body>
</html>
