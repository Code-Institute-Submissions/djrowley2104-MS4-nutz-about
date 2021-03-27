function updatePrice(event){
    let selectedOption = event.target.options[event.target.selectedIndex]
    document.getElementById('currentPrice').innerHTML = '£' + selectedOption.getAttribute('data-value');
}
document.getElementById('id_product_size').addEventListener("change", updatePrice);