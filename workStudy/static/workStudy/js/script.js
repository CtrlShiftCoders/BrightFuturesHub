// Script to set filter buttons on job listings page

const container = document.getElementById("listings")
const btnContainer = document.getElementById("filterBtns")
const job_list = Array.from(document.getElementsByClassName("Jobs"))

let filters = []
const Categories = ["Internship", "Remote Job", "Job"]

Categories.forEach((category) => {
    const btn = document.createElement("button");
    btn.classList.add("filterBtn");
    btn.textContent = category;
    btnContainer.append(btn)
    btn.addEventListener("click", () => {
        console.log(btn.textContent)
        if (filters.indexOf(btn.textContent) != -1) {
            filters.splice(filters.indexOf(btn.textContent),1)
            btn.style.backgroundColor = "white"
        } else {
            filters.push(btn.textContent)
            btn.style.backgroundColor = "blue"
        }
        filter()
    })
});
console.log(Array.from(job_list));

function filter() {
    while (container.firstChild) {
    container.removeChild(container.firstChild);
    }
    
    Array.from(job_list).forEach((elem) => {
        if (filters.length!=0){
            if (filters.includes(elem.lastElementChild.textContent)) {
                console.log(elem.lastElementChild.textContent);
                
                container.appendChild(elem)
            }
        } else {
            container.appendChild(elem)
        }
    });
}
