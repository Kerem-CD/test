/* <div><img class="pic" src="/profilepic/{{token}}/{{name}}" ></img><h4 class="name">   Name</h4><p>Content</p></div>*/
document.addEventListener('DOMContentLoaded', function() {
    fetch("/getmessage/" + document.getElementById("token").innerHTML).then(response => {
        return response.json();
    }).then(data => {
        for (var i = 0; i < data.length; i++) {
            var div = document.createElement("div");
            var img = document.createElement("img");
            img.setAttribute("class", "pic");
            img.setAttribute("src", "/profilepic/" + document.getElementById("token").innerHTML + "/" + data[i]["who"]);
            var h4 = document.createElement("h4");
            h4.setAttribute("class", "name");
            h4.innerHTML = "    "+data[i]["who"];
            var p = document.createElement("p");
            p.innerHTML = data[i]["post"];
            div.appendChild(img);
            div.appendChild(h4);
            div.appendChild(p);
            document.body.appendChild(div);
        }
    })
    document.getElementById("ok").addEventListener("click", function() {
        fetch("/addmessage/"+document.getElementById("token").innerHTML+"?message="+document.getElementById("post").value).then(response => {
            location.reload();
        })
    });
});