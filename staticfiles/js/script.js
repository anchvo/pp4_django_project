document.addEventListener("DOMContentLoaded", function () {
  
  // Flatpickr initialization for the appointment date field
  flatpickr("#id_appointment_date", {
    enableTime: true,
    dateFormat: "Y-m-d H:i", // Date and time format
    defaultHour: 12, // Default time (optional)
    defaultMinute: 0, // Default minutes (optional)
    minuteIncrement: 5, // Allow incrementing by 5 minutes
    time_24hr: true, // Use 24-hour format
    minDate: "today"  // Prevent selecting a past date
  });

  // Function to update the doctor dropdown based on selected specialization and location
  const updateDoctors = function () {
    const specField = document.getElementById("id_doctor_specialisation");
    const locField = document.getElementById("id_doctor_location");
    const doctorSelect = document.getElementById("id_doctor");

    if (!specField || !locField || !doctorSelect) {
      console.warn("Skipping doctor update – one or more fields not found.");
      return;
    }

    const specialisation = specField.value;
    const location = locField.value;

    if (specialisation && location) {
      fetch(`/get-doctors/?specialisation=${specialisation}&location=${location}`)
        .then((response) => response.json())
        .then((data) => {
          doctorSelect.innerHTML = ""; // Clear existing options

          const defaultOption = document.createElement("option");
          defaultOption.text = "Select Doctor";
          doctorSelect.appendChild(defaultOption);

          if (data.doctors.length === 0) {
            document.getElementById("no-doctor-message").style.display = "block";
            doctorSelect.disabled = true;
          } else {
            document.getElementById("no-doctor-message").style.display = "none";
            doctorSelect.disabled = false;

            data.doctors.forEach((doctor) => {
              const option = document.createElement("option");
              option.value = doctor.id;
              option.text = doctor.full_name;
              doctorSelect.appendChild(option);
            });
          }
        })
        .catch((error) => {
          console.error("Error fetching doctors:", error);
        });
    }
  };

  try {
    const specField = document.getElementById("id_doctor_specialisation");
    const locField = document.getElementById("id_doctor_location");

    if (specField && locField) {
      specField.addEventListener("change", updateDoctors);
      locField.addEventListener("change", updateDoctors);
    } else {
      console.warn("Skipping doctor update – Specialisation or Location fields are not found.");
    }

  } catch (e) {
    console.error("Form error:", e.message);
  }

  // Modal for Delete Appointment functionality
  const deleteButtons = document.querySelectorAll(".btn-delete-appointment");
  const deleteForm = document.getElementById("deleteForm");

  deleteButtons.forEach(button => {
    button.addEventListener("click", function () {
      const appointmentId = this.getAttribute("data-appointment_id");
      const baseUrl = this.getAttribute("data-delete-url").replace(/0\/?$/, "");
      
      // Ensure attributes are available before proceeding
      if (appointmentId && baseUrl) {
        deleteForm.action = `${baseUrl}${appointmentId}/`;
      } else {
        console.warn("Missing appointment ID or delete URL attribute on delete button.");
      }
    });
  });

});