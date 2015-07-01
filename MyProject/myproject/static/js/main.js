$(document).ready(function() {
    
    var socket = io.connect('http://127.0.0.1:6543/chat');
    
    $(window).bind("beforeunload", function() {
        socket.disconnect();
    });
    
    $('#countButton').click(function() {
        var nbTimes = $('#numberInput').val();
        if(nbTimes == "")
        {
            alert("Enter a value!")
        }
        else 
        {
            socket.emit("count", nbTimes);
        }
    });
    
    socket.on("chat", function(e) {
        console.log(e);
    })
    
    socket.on("count_response", function(e) {
        var box = $("#logs");
        box.val(box.val() + e.value + "   ");
    })
    
})
