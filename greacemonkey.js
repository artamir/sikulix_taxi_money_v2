// ==UserScript==
// @name     Скрипт БезИмени 930294
// @version  1
// @grant    none
// ==/UserScript==
function displayNone() {
    //e = document.querySelectorAll('.oImage,.oTime,.oPower,.oAddress,.party-order-container,.level-block,.d-block,.spo-block');
    e = document.querySelectorAll('.d-block,.spo-block');
    for (var i = 0; i < e.length; i++) {
        e[i].style.display = 'none';
    }

    e = document.querySelectorAll('.oInner');
    for (var i = 0; i < e.length; i++) {
        //e[i].style.width = '332px';
        //e[i].style.height = '141.133px';
    }
}

function orderPriceFont(){
  fn = "orderPriceFont"
  //alert(fn)
	e = document.querySelectorAll('[data-control="price"]');
  for (var i = 0; i < e.length; i++) {
  	//alert(e[i])
    if (e[i].textContent.indexOf("Д:") == -1) {
    	e[i].textContent = "Д: "+e[i].textContent
    	e[i].style.setProperty('font-family','OCR-B',"important");
    	e[i].style.setProperty('font-weight','bold',"important");
    	e[i].style.setProperty('font-size','large',"important");
    }  
	}
}

function getAllNextSiblings(element) {
    var out = [];
    while (element.nextSibling) {
        out.push(element = element.nextSibling);
    }

    return out;
}

function getAllPreviousSiblings(element) {
    var out = [];
    while (element.previousSibling) {
        out.push(element = element.previousSibling);
    }

    return out;
}

function getAllSiblings(element, include) {
    var out = getAllNextSiblings(element);
    out.concat(getAllPreviousSiblings(element));
    if (include)
        out.push(element);

    return out;
}

function maxOrder() {
    //alert("max order")
    e = document.querySelectorAll('.oPrice');
    maxBonusPrice = 0.00;
    maxBonusElement = "";
    maxHalturaPrice = 0.00;
    maxHalturaElement = "";
    maxRabotaPrice = 0.00;
    maxRabotaElement = "";
    for (var i = 0; i < e.length; i++) {
        t = getAllNextSiblings(e[i].parentElement);
        for (var j = 0; j < t.length; j++) {
            if (t[j].textContent.indexOf("Бонус") > -1) {
                var price = parseFloat(e[i].textContent);
                //alert(price);
                if (price > maxBonusPrice) {
                    maxBonusPrice = price;
                    maxBonusElement = t[j];
                }
            }
            if (t[j].textContent.indexOf("Халтура") > -1) {
                var price = parseFloat(e[i].textContent);
                //alert(price);
                if (price > maxHalturaPrice) {
                    maxHalturaPrice = price;
                    maxHalturaElement = t[j];
                }
            }
            if (t[j].textContent.indexOf("РАБОТА") > -1) {
                var price = parseFloat(e[i].textContent);
                //alert(price);
                if (price > maxRabotaPrice) {
                    maxRabotaPrice = price;
                    maxRabotaElement = t[j];
                }
            }
        }

    }

    maxElement = maxBonusElement;
    color = "red"
	if (maxElement != "") {
		if (maxBonusElement.textContent.indexOf("макс") == -1) {
			maxElement.textContent = maxElement.textContent + "-макс\nmax"
				el = maxElement.parentElement.parentElement.parentElement;
			el.style.setProperty("outline", "1px solid " + color, "important")
		}
	}

    maxElement = maxHalturaElement;
    color = "blue"
	if (maxElement != "") {
		if (maxElement.textContent.indexOf("макс") == -1) {
			maxElement.textContent = maxElement.textContent + "-макс\nmax"
				el = maxElement.parentElement.parentElement.parentElement;
			el.style.setProperty("outline", "1px solid " + color, "important")
		}
	}

    maxElement = maxRabotaElement;
    color = "green"
	if (maxElement != "") {
		if (maxElement.textContent.indexOf("макс") == -1) {
			maxElement.textContent = maxElement.textContent + "-макс\nmax"
				el = maxElement.parentElement.parentElement.parentElement;
			el.style.setProperty("outline", "1px solid " + color, "important")
		}
	}
        //alert(maxPrice);
}

displayNone();
//alert(2);
document.addEventListener("DOMAttrModified", function () {
    //  alert(3);
    displayNone();
    maxOrder();
    orderPriceFont();
});

window.onload = function () {
    displayNone();
    maxOrder();
    orderPriceFont()
};
