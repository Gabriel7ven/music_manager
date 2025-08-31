const btnCopiarCronograma = document.getElementById('copiar-cronograma');

btnCopiarCronograma.addEventListener('click', copiarCronograma)

function copiarCronograma() {
    const moment = document.getElementsByClassName('moment-name');
    const music = document.getElementsByClassName('music-name');
    const reference = document.getElementsByClassName('music-reference');
    const number = document.getElementsByClassName('music-number');
    console.log(number);
    let musicItem = "";

    let momentsArray = [];
    for(let i=0; i < moment.length; i++) {

        if(momentsArray.includes(moment[i].innerText)) {
            console.log(`Momento ${moment[i].innerText} já incluído`);
        }else{
            musicItem += "\n*" + moment[i].innerText + "*" + ":\n";
            momentsArray.push(moment[i].innerText);   
        }
        

        // musicItem += "\t" + music[i].innerText + " - " + reference[i].innerText + (number[i] ? " " + number[i].innerText : "");
        musicItem += "\t" + reference[i].innerText + (number[i] ? " " + number[i].innerText : "") + "  -  " + music[i].innerText;
        // if (number[i]) {
        //     musicItem += "  " + number[i].innerText;
        // }
        musicItem += "\n";
    }
    console.log(musicItem);
    navigator.clipboard.writeText(musicItem);
    // btnCopiarCronograma.style.backgroundColor = 'lightgreen';
    alert("Texto copiado com sucesso!");
}

// const btnDelete = document.getElementById("update");

// btnDelete.addEventListener('click', askDelete);

// function askDelete(){



// }

