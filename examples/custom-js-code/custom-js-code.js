
// Define your "run" function here
function run (formData, formLayout) {
    // This function will be called when form values change
    // formData: the data that is set on the form
    // formLayout: the layout of the form, you can change the layout to show error messages or other ui elements
    window.dl.sendEvent({
        name: "app:toastMessage",
        payload: {
            "type": "info", // info, error, warning, success
            "message": 'Toasting from JS code'
        },
    });
    // Set an error message on the component if the name is too short
    if (formData.wonderland_name.length < 100) {
        formLayout[0].components[0].errorMessage = `The name is too short, Min 100 characters. ${formData.wonderland_name.length}/100`
    }
    else {
        formLayout[0].components[0].errorMessage = null
    }
    // Log the form data to the console
    console.log('Consoling from the JS code');

    // Return the form layout and data
    return { formLayout, formData };
}

// Export the run function
module.exports = {run};
