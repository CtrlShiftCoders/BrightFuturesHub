// Script to set filter buttons on job listings page

const container = document.getElementById("listings")
const btnContainer = document.getElementById("filterBtns")
const job_list = Array.from(document.getElementsByClassName("Jobs"))
let filters = []
const Categories = ["Internship", "Remote Job", "On Site Job"]

Categories.forEach((category) => {
    const btn = document.createElement("button");
    btn.classList.add("filterBtn");
    btn.classList.add("btn");
    btn.classList.add("btn-outline-info");
    console.log(btn.classList);
    
    btn.textContent = category;
    btnContainer.append(btn)
    btn.addEventListener("click", () => {
        if (filters.indexOf(btn.textContent) != -1) {
            filters.splice(filters.indexOf(btn.textContent), 1)
            btn.classList.remove("btn-info")
            btn.classList.add("btn-outline-info");
        } else {
            filters.push(btn.textContent)
            btn.classList.add("btn-info")
            btn.classList.remove("btn-outline-info");
        }
        filter()
    })
});

function filter() {
    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }

    Array.from(job_list).forEach((elem) => {
        if (filters.length != 0) {
            // last child contains category
            if (filters.includes(elem.lastElementChild.textContent)) {
                container.appendChild(elem)
            }
        } else {
            container.appendChild(elem)
        }
    });
}
