function lagreinfo() {
    var input1 = document.getElementById("input1").value;
    var input2 = document.getElementById("input2").value;
    console.log("log")
    console.log(input1)
    console.log(input2)
    alert(input1 +" og "+ input2);
    payload = JSON.stringify({
            tittel: input1,
            innhold: input2
        })
    console.log("payload" + payload)
    fetch("http://127.0.0.1:8000/notater", {
        method: "POST",
        body: payload,
        headers: {'Content-Type': 'application/json'},

    })
}

function hentinfo() {
    fetch("http://127.0.0.1:8000/notater", {
        method: "GET",
        headers: {'Content-Type': 'application/json'}

    })
}

// fetch("http://127.0.0.1:5500/Klient/index.html", {
//     method: "POST",
//     body: JSON.stringify({
//         userID: 1,
//         title: "Tittel her",
//         innhold: "Innholdet her",
//         completed: false
//     }),
// });

//async function sendData() {
//    try {
//      const response = await fetch('http://127.0.0.1:8000/notater', {
//        method: 'POST',
//        headers: {
//          'Content-Type': 'application/json'
//        },
//        body: JSON.stringify({
//          tittel: "Tittel her",
//          innhold: "Innhold her"
//        })
//      });
//   
//      if (!response.ok) {
//        throw new Error(response.message);
//      }
//   
//      const data = await response.json();
//      console.log('Svar fra server:', data);
//   
//    } catch (error) {
//      console.error('Feil:', error);
//    }
//  }
   
