const listItems = document.querySelectorAll(".list");
const indicator = document.querySelector(".indicator");

function activeLink() {
    listItems.forEach(item => {
        item.classList.remove("active");
    });

    this.classList.add("active");

    // Move the indicator
    const index = Array.from(listItems).indexOf(this);
    indicator.style.transform = `translateX(${index * 70}px)`;
}

listItems.forEach(item => {
    item.addEventListener("click", activeLink);
});
