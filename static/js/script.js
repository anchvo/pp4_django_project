document.addEventListener("DOMContentLoaded", function () {
  // Initialize the Flatpickr for the appointment date field
  flatpickr("#id_appointment_date", {
    enableTime: true,
    dateFormat: "Y-m-d H:i", // Date and time format
    defaultHour: 12, // Default time (optional)
    defaultMinute: 0, // Default minutes (optional)
    minuteIncrement: 5, // Allow incrementing by 5 minutes
    time_24hr: true, // Use 24-hour format
    minDate: "today"  // Prevent selecting a past date
  });

  // Function to update the doctor dropdown
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

    if (!specField || !locField) {
      throw new Error("Specialisation or Location fields not found.");
    }

    specField.addEventListener("change", updateDoctors);
    locField.addEventListener("change", updateDoctors);

  } catch (e) {
    console.error("Form error:", e.message);
  }
});