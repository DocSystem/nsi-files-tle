/* CONFIG SECTION */

const SPEED = 100;              // Vitesse entre 1 et 1000
const TAB = [4,12,3,14,5,-9,8]; // Tableau à trier

/* END CONFIG SECTION */

async function tri_a_bulles(tab) {
    let n = tab.length;
    for (let i = 0; i < n-1; i++) {
        for (let j = n-1; j > i; j--) {
            if (tab[j] < tab[j-1]) {
                let tmp = tab[j];
                tab[j] = tab[j-1];
                tab[j-1] = tmp;
                await mettre_a_jour_liste(tab);
            }
        }
    }
}

function afficher_liste(tab) {
    var liste = document.querySelector("#liste");
    liste.innerHTML = "";
    for (let i in tab) {
        liste.innerHTML += "<div class='liste_elem' id='elem_" + tab[i] + "' style='top: 10px; left: " + (i*40 + 10) + "px'>" + tab[i] + "</div>";
    }
}

function copyTab(tab) {
    let newTab = [];
    for (let i in tab) {
        newTab[i] = tab[i];
    }
    return newTab;
}

async function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function mettre_a_jour_liste(tab) {
    for (let i in tab) {
        if (oldTab[i] != tab[i]) {
            let elem = document.querySelector("#elem_" + oldTab[i]);
            while (elem.style.top != "50px") {
                elem.style.top = parseInt(elem.style.top) + 1 + "px";
                await wait(1000/SPEED);
            }
            while (elem.style.left != (tab.indexOf(oldTab[i])*40 + 10) + "px") {
                if (parseInt(elem.style.left.split("px")[0]) < (tab.indexOf(oldTab[i])*40 + 10)) {
                    elem.style.left = parseInt(elem.style.left.split("px")[0]) + 1 + "px";
                    await wait(1000/SPEED);
                }
                else {
                    elem.style.left = parseInt(elem.style.left.split("px")[0]) - 1 + "px";
                    await wait(1000/SPEED);
                }
            }
            while (elem.style.top != "10px") {
                elem.style.top = parseInt(elem.style.top) - 1 + "px";
                await wait(1000/SPEED);
            }
        }
    }
    for (let i in tab) {
        oldTab[i] = tab[i];
    }
    return true;
}

var tab = copyTab(TAB);
var oldTab = copyTab(TAB);

afficher_liste(tab);
tri_a_bulles(tab);
