const formSelector = "form#subsection-form";

const getSubsectionFormData = function() {
    return new FormData(document.querySelector(formSelector));
}

const beforeUnloadHandler = function(event) {
  event.preventDefault();
  event.returnValue = true;
};

const setupInputListener = function(originalFormData) {
    const elements = document.querySelectorAll(
        `${formSelector} input, ${formSelector} select, ${formSelector} textarea`,
    );

    for (const element of elements) {
        element.addEventListener("input", function() {
            let currentFormData = getSubsectionFormData();
            let isFormChanged = false;

            for (let [key, value] of currentFormData.entries()) {
                if (originalFormData.get(key) !== value) isFormChanged = true;
            }

            if (isFormChanged) {
                window.addEventListener("beforeunload", beforeUnloadHandler);
            } else {
                window.removeEventListener("beforeunload", beforeUnloadHandler);
            }
        });
    }
}

const setupFormSubmissionListener = function() {
    const form = document.querySelector(formSelector);
    form.addEventListener("submit", function() {window.removeEventListener("beforeunload", beforeUnloadHandler);});
}

document.addEventListener("DOMContentLoaded", function() {
    originalFormData = getSubsectionFormData();
    setupInputListener(originalFormData);
    setupFormSubmissionListener()
})
