document.addEventListener("DOMContentLoaded", function () {
    const division = document.getElementById("id_division");
    const district = document.getElementById("id_district");
    const thana = document.getElementById("id_thana");

    if (!division || !district || !thana) return;

    division.addEventListener("change", function () {
        const val = this.value;
        fetch(`/districts/?division=${encodeURIComponent(val)}`)
            .then((res) => res.json())
            .then((data) => {
                district.innerHTML = '<option value="">---------</option>';
                data.districts.forEach((d) => {
                    district.innerHTML += `<option value="${d}">${d}</option>`;
                });
                thana.innerHTML = '<option value="">---------</option>'; // reset thanas
            });
    });

    district.addEventListener("change", function () {
        const val = this.value;
        fetch(`/thanas/?district=${encodeURIComponent(val)}`)
            .then((res) => res.json())
            .then((data) => {
                thana.innerHTML = '<option value="">---------</option>';
                data.thanas.forEach((t) => {
                    thana.innerHTML += `<option value="${t}">${t}</option>`;
                });
            });
    });
});
