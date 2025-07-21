
// Define your "run" function here
function run (formData, formLayout) {
    // This function will be called when form values change
    // formData: the data that is set on the form
    // formLayout: the layout of the form, you can change the layout to show error messages or other ui elements
    // Set an error message on the component if the name is too long
    if (formData.text2.length > 10) {
        formLayout[0].components[32].errorMessage = `The name is too long, Max 10 characters. ${formData.text2.length}/10`;
        window.dl.sendEvent({
            name: "app:toastMessage",
            payload: {
                "type": "info", // info, error, warning, success
                "message": 'The name is too long...'
            },
        });
    }
    else {
        formLayout[0].components[32].errorMessage = ''
    }
    // Log the form data to the console
    console.log('Consoling from the JS code');

    // Return the form layout and data
    return { formLayout, formData };
}

// Export the run function
module.exports = {run};