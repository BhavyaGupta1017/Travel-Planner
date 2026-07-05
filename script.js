const form = document.getElementById("travelForm");

form.addEventListener("submit", async function(e){

e.preventDefault();

document.getElementById("loading").style.display="block";

document.getElementById("result").innerHTML="";

const data={

source:document.getElementById("source").value,

destination:document.getElementById("destination").value,

budget:document.getElementById("budget").value,

days:document.getElementById("days").value,

travellers:document.getElementById("travellers").value,

transport:document.getElementById("transport").value,

hotel:document.getElementById("hotel").value,

interest:document.getElementById("interest").value

};

try{

const response=await fetch("/plan",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(data)

});

const result=await response.json();

document.getElementById("loading").style.display="none";

document.getElementById("result").textContent=result.plan;

}

catch(error){

document.getElementById("loading").style.display="none";

document.getElementById("result").innerHTML="❌ Error connecting to AI.";

}
document.getElementById("mapFrame").src =
`https://www.google.com/maps?q=${data.destination}&output=embed`;
document.getElementById("destinationImage").src =
`https://source.unsplash.com/1200x500/?${data.destination},travel`;

});