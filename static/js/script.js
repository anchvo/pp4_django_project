console.log("Test, that collecting static files works");

// Function to filter Doctors based on Specialisation and Location
function updateDoctors() {
    var specialisation = document.getElementById("id_doctor_specialisation").value;
    var location = document.getElementById("id_doctor_location").value;

    // Only proceed if both specialisation and location are selected
    if (specialisation && location) {
        fetch(`/get-doctors/?specialisation=${specialisation}&location=${location}`)
            .then(response => response.json())
            .then(data => {
                var doctorSelect = document.getElementById("id_doctor");
                doctorSelect.innerHTML = '';  // Clear existing options
                var defaultOption = document.createElement('option');
                defaultOption.text = "Select Doctor";
                doctorSelect.appendChild(defaultOption);

                data.doctors.forEach(doctor => {
                    var option = document.createElement('option');
                    option.value = doctor.id;
                    option.text = doctor.full_name;
                    doctorSelect.appendChild(option);
                });
            });
    }
}

// Attach Event Listeners to the fields Specialisation and Location
document.getElementById("id_doctor_specialisation").addEventListener("change", updateDoctors);
document.getElementById("id_doctor_location").addEventListener("change", updateDoctors);