/**
 * Created by summerlynbryant on 8/27/15.
 */


var inventory = document.getElementById('inventory');
var woodstock, material, price;

function Product(name, stock, price) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function (num) {
        this.stock -= num;
    };

    this.inStock = function () {
        return this.stock > 0;
    };


}

var materials = [];

populateInventoryDOM();

function populateInventoryDOM() {
    // Loop through materials
    // Add a row for each item in materials into the inventory
    // Make sure that stock class reflects inStock
    // Make sure that checkbox status reflects checked
    for (var i = 0; i < materials.length; i++) {
        var newProdRow = document.createElement('tr');

        // Checkbox column
        var checkboxCell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        checkbox.checked = materials[i].checked;
        checkboxCell.appendChild(checkbox);
        newProdRow.appendChild(checkboxCell);

        // Name Column
        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(materials[i].name);
        nameCol.appendChild(nameText);
        newProdRow.appendChild(nameCol);

        // Price Column
        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + materials[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        // Stock Column
        var stockCol = document.createElement('td');
        stockCol.className = materials[i].inStock();
        var stockText = document.createTextNode(materials[i].stock);
        stockCol.appendChild(stockText);
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);
    }

}
//
//function checkAllHandler(e) {
//    console.log(e);
//    var inputs = inventory.getElementsByTagName('input');
//    for (var i = 0; i < inputs.length; i++) {
//        if (inputs[i].type == 'checkbox') {
//            inputs[i].checked = e.target.checked;
//        }
//    }
//}
////checkAll = document.getElementById('checkAll');
////checkAll.addEventListener('click', function (e) {
////    checkAllHandler(e, 6);
////}, false);

function removeStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs.length > 0) {
            if (inputs[0].type == 'checkbox') {
                if (inputs[0].checked) {
                    // Flip the status of the stock column
                    var stock = rows[i].lastElementChild;
                    stock.className = 'false';
                    stock.textContent = 'No';
                }
            }
        }
    }
}

function addStock() {
    var rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type == 'checkbox') {
            if (inputs[0].checked) {
                // Flip the status of the stock column
                var stock = rows[i].lastElementChild;
                stock.className = 'true';
                stock.textContent = 'Yes';
            }
        }
    }
}

function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    if (material === '' || price === '' || isNaN(price)) {
        return
    }

    var newProdRow = document.createElement('tr');

    // Checkbox column
    var checkboxCell = document.createElement('td');
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.checked = false;
    checkboxCell.appendChild(checkbox);
    newProdRow.appendChild(checkboxCell);

    // Name Column
    var nameCol = document.createElement('td');
    var nameText = document.createTextNode(material);
    nameCol.appendChild(nameText);
    newProdRow.appendChild(nameCol);

    // Price Column
    var priceCol = document.createElement('td');
    var priceText = document.createTextNode('$' + price);
    priceCol.appendChild(priceText);
    newProdRow.appendChild(priceCol);

    // Stock Column
    var stockCol = document.createElement('td');
    stockCol.className = 'true';
    var stockText = document.createTextNode('10');
    stockCol.appendChild(stockText);
    newProdRow.appendChild(stockCol);

    inventory.appendChild(newProdRow);
    materials.push(new Product(material, 10, price));

    //var newRow = '<tr>';
    //newRow += '<td><input type="checkbox"/></td>';
    //newRow += '<td>' + material + '</td>';
    //newRow += '<td>$' + price + '</td>';
    //newRow += '<td class="false">No</td>';
    //newRow += '</tr>';

    //inventory.innerHTML += newRow;

    document.getElementById('material').value = '';
    document.getElementById('price').value = '';
}

// Make an JSON call to get the data from the server
var xhr = new XMLHttpRequest();

xhr.onload = function () {
    console.log("HEYO!");
    if (xhr.status === 200) {
        responseObject = JSON.parse(xhr.responseText);
        console.log(responseObject.inventory);

        var newInventory = "";
        var responseInventory = responseObject.inventory.item;
        console.log("SUP");
        for (var i = 0; i < responseInventory.length; i++) {
            console.log(responseObject.inventory);
            newInventory += '<tr>';
            console.log("Suck it json");
            newInventory += '<td><input type="checkbox"/></td>';
            newInventory += '<td>' + responseInventory[i].name + '</td>';
            newInventory += '<td>$' + responseInventory[i].price + '</td>';
            newInventory += '<td>' + responseInventory[i].numInStock + '</td>';
            newInventory += '</tr>';
            console.log(newInventory);

        }

        document.getElementById("inventory").innerHTML = newInventory;
    }

};



xhr.open("GET", "data_json/stock.json", true);
xhr.send(null);