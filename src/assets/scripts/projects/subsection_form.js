class SubsectionForm {
    constructor() {
        this.formSelector = "form#subsection-form";
        this.originalFormData = this.getSubsectionFormData();
        this.setupInputListener();
        this.setupFormSubmissionListener()
    }

    getSubsectionFormData() {
        return new FormData(document.querySelector(this.formSelector));
    }

    beforeUnloadHandler(event) {
      event.preventDefault();
      event.returnValue = true;
    };

    setupInputListener() {
        const elements = document.querySelectorAll(
            `${this.formSelector} input, ${this.formSelector} select, ${this.formSelector} textarea`,
        );

        for (const element of elements) {
            element.addEventListener("input", () => {
                let currentFormData = this.getSubsectionFormData();
                let isFormChanged = false;

                for (let [key, value] of currentFormData.entries()) {
                    if (this.originalFormData.get(key) !== value) isFormChanged = true;
                }

                if (isFormChanged) {
                    window.addEventListener("beforeunload", this.beforeUnloadHandler);
                } else {
                    window.removeEventListener("beforeunload", this.beforeUnloadHandler);
                }
            });
        }
    }

    setupFormSubmissionListener() {
        const form = document.querySelector(this.formSelector);
        form.addEventListener("submit", () => {window.removeEventListener("beforeunload", this.beforeUnloadHandler);});
    }
}

document.addEventListener("htmx:after:swap", function() {
    new SubsectionForm();
})
