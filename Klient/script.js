function lagreinfo() {
    var input1 = document.getElementById("input1").value;
    var input2 = document.getElementById("input2").value;
    console.log("log")
    console.log(input1)
    console.log(input2)
    alert(input1, input2);
}

fetch("http://127.0.0.1:5500/Klient/index.html", {
    method: "POST",
    body: JSON.stringify({
        userID: 1,
        title: "Tittel her",
        innhold: "Innholdet her",
        completed: false
    }),
});