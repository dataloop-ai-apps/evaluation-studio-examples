# Evaluation Studio

A powerful web-based application designed for evaluating Large Language Model (LLM) performance through interactive layouts and dynamic components.

## Features

-   **Studio Builder**: Design custom evaluation layouts with drag-and-drop interface
-   **Studio Evaluator**: Run and analyze LLM performance
-   **Dynamic Components**: Support for multiple input/output types
-   **Dataset Integration**: Seamless integration with Dataloop platform
-   **Custom Styling**: Add custom CSS for form styling
-   **Form Validation**: Add custom JavaScript for form validation and dynamic behavior
-   **Hierarchical Forms**: Support for conditional form fields based on parent values

## Components Library

<details>
<summary>Common Properties</summary>

All components support these base properties:

-   `key` (string, required): Unique identifier for the field
-   `type` (string, required): Component type identifier
-   `title` (string): Display title for the field
-   `tooltip` (string): Hover tooltip text
-   `hidden` (boolean): Whether the component should be hidden
-   `required` (boolean): Whether the field is required
-   `hierarchy` (object): Conditional visibility rules
    -   `condition` (string): DQL condition to evaluate

</details>

<details>
<summary>Input Components</summary>

### Title

-   Type: `title`
-   Properties:
    -   All common properties
    -   `placeholder` (string): Placeholder text

### Text Input

-   Type: `text`
-   Properties:
    -   All common properties
    -   `placeholder` (string): Placeholder text
    -   `disabled` (boolean): Whether the field is disabled
    -   `errorMessage` (string): Error message to display

### Select

-   Type: `select`
-   Properties:
    -   All common properties
    -   `options` (array, required): Array of options
        -   `label` (string): Display text
        -   `value` (any): Option value
    -   `disabled` (boolean): Whether the field is disabled

### Radio Group

-   Type: `radio`
-   Properties:
    -   All common properties
    -   `options` (array, required): Array of options
        -   `label` (string): Display text
        -   `value` (any): Option value
    -   `disabled` (boolean): Whether the field is disabled

### Checkbox Group

-   Type: `checkbox`
-   Properties:
    -   All common properties
    -   `options` (array, required): Array of options
        -   `label` (string): Display text
        -   `value` (any): Option value
    -   `disabled` (boolean): Whether the field is disabled

### Slider

-   Type: `slider`
-   Properties:
    -   All common properties
    -   `min` (number): Minimum value
    -   `max` (number): Maximum value
    -   `default` (number): Default value
    -   `step` (number): Step increment
    -   `disabled` (boolean): Whether the field is disabled

</details>

<details>
<summary>Media Components</summary>

### Image Viewer

-   Type: `image`
-   Properties:
    -   All common properties

### Audio Viewer

-   Type: `audio`
-   Properties:
    -   All common properties

### Video Viewer

-   Type: `video`
-   Properties:
    -   All common properties

### URL Viewer

-   Type: `url`
-   Properties:
    -   All common properties
    -   `initialWidth` (number): Initial iframe width
    -   `initialHeight` (number): Initial iframe height

### Markdown Viewer

-   Type: `markdown`
-   Properties:
    -   All common properties
    -   `content` (string): Markdown content to render

</details>

<details>
<summary>Special Components</summary>

### Star Rating

-   Type: `rating`
-   Properties:
    -   All common properties
    -   `maxStars` (number): Maximum number of stars (default: 5)
    -   `showValue` (boolean): Whether to show numeric value

### Conversation

-   Type: `conversation`
-   Properties:
    -   All common properties

</details>

## Studio Builder

The Studio Builder provides a drag-and-drop interface for creating custom evaluation layouts.

### Layout Structure

Layouts are defined in JSON format with the following structure:

```json
{
  "sections": [
    {
      "title": "Section Title",
      "hidden": false,  // Optional: hide/show entire section
      "layout": {
        "direction": "vertical|horizontal",
        "wrap": true|false
      },
      "components": [
        {
          "type": "text",
          "key": "textInput1",
          "title": "Text Input",
          "placeholder": "Enter text...",
          "tooltip": "Help text",
          "required": true,
          "hidden": false  // Optional: hide/show component
        }
      ]
    }
  ]
}
```

### Visibility Control

Components and sections can be hidden in three ways:

1. **Direct hiding**: Use the `hidden` property

```json
{
    "type": "text",
    "key": "hiddenField",
    "hidden": true
}
```

2. **Hierarchical fields**: Make visibility conditional on other field values

```json
{
    "type": "text",
    "key": "childField",
    "title": "Child Field",
    "hierarchy": {
        "condition": { "tea_party_size": { "$eq": "6" } }
    }
}
```

More examples:

-   Show if riddle answer contains "raven":

```json
{
    "condition": { "riddle_answer": { "$ilike": "*raven*" } }
}
```

-   Use AND logic to show if tea party size is 42 and time is frozen:

```json
  "condition": {
            "$and": [
              {
                "tea_party_size": {
                  "$eq": "42"
                }
              },
              {
                "time_frozen": true
              }
            ]
          }
```

-   Use OR logic to show if tea party size is 42 or time is frozen:

```json
{
    "condition": {
        "$or": [
            {
                "tea_party_size": {
                    "$eq": "0"
                }
            },
            {
                "tea_party_size": {
                    "$eq": "infinity"
                }
            }
        ]
    }
}
```

-   Use IN logic to show if tea party size is 0, 42 or infinity:

```json
{
    "condition": {
        "tea_types": {
            "$in": ["earl_grey", "darjeeling"]
        }
    }
}
```

-   Use EXISTS logic to show if tea party size is not 0:

```json
{
    "condition": {
        "riddle_answer": {
            "$exists": true
        }
    }
}
```

-   Advance exmaple:

```json
{
    "condition": {
        "$or": [
            {
                "$and": [
                    {
                        "tea_party_size": {
                            "$eq": "6"
                        }
                    },
                    {
                        "time_frozen": true
                    }
                ]
            },
            {
                "$and": [
                    {
                        "tea_types": {
                            "$in": ["chamomile"]
                        }
                    },
                    {
                        "riddle_answer": {
                            "$exists": true
                        }
                    }
                ]
            }
        ]
    }
}
```

1. **Dynamic hiding**: Use JavaScript to control visibility

```javascript
module.exports = {
    run: async function (formData, formLayout) {
        // Hide field based on some condition
        formLayout[0].components[0].hidden = someCondition;
        return {
            formData,
            formLayout,
        };
    },
};
```

## JS and CSS for Dynamic Behavior

### JavaScript Module

Add custom validation and dynamic behavior by providing a JavaScript module:

```javascript
module.exports = {
    run: async function (formData, formLayout) {
        // Modify form data or layout
        return {
            formData: modifiedData,
            formLayout: modifiedLayout,
        };
    },
};
```

### Custom CSS

Add custom styling by providing CSS:

```css
.form-section {
    /* Custom section styling */
}

.field-container {
    /* Custom field styling */
}
```

## Studio Evaluator

### Usage

The evaluator allows you to:

1. Load predefined layouts
2. Run evaluations against LLMs
3. Collect and analyze results
4. Add review flags and issue markers to responses

### Integration Script

Use the following Python script to upload evaluation items:

```python
import dtlpy as dl
import io

# Get the dataset
dataset = dl.datasets.get(dataset_id='${datasetId}')

# Create a io.BytesIO object from the data json
data = ${JSON.stringify(formData, null, 2)}
buffer = io.BytesIO(data)

item = dataset.items.upload(
    file=buffer,
    name='${formName}-data.json',
    metadata={
        'system': {
            'shebang': {
                'dltype': 'evaluation-studio'
            },
            'evaluation': {
                'layoutName': '${formName}'
            }
        }
    }
)

print("Item uploaded successfully:", item.id)
print("Open in platform:", item.platform_url)
```

## Form Validation

The Studio supports two types of validation:

### 1. Built-in Required Field Validation

Components can be marked as required using the `required` property:

```json
{
    "type": "text",
    "key": "requiredField",
    "title": "Required Field",
    "required": true
}
```

### 2. Custom JavaScript Validation

Add custom validation logic by providing a JavaScript module that exports a `run` function:

```javascript
module.exports = {
    run: async function (formData, formLayout) {
        // Modify form data or layout
        // Perform custom validation
        return {
            formData: modifiedData, // Optional: modified form data
            formLayout: modifiedLayout, // Optional: modified layout
            validationResult: {
                pass: true | false, // Validation result
                errorMessage: "Error message if validation fails",
            },
        };
    },
};
```

### Validation Results

The validation system returns a `FormJsResult` object containing:

-   `missingRequiredFields`: Array of required fields that are empty
-   `runScript`: Results from custom validation including:
    -   Modified form data and layout
    -   Validation result with pass/fail status and error message

### Working in Tasks and Assignments

Form validation is automatically performed when a status change is activated on an item from a task.

Failed validations will:

1. Block status changes
2. Display error messages
3. Show custom validation error messages

### Auto-save and Validation

The form implements debounced auto-saving that:

-   Triggers validation before saving
-   Saves changes after 2 seconds of inactivity
-   Tracks modifications using deep comparison
-   Preserves complex data structures (arrays, nested objects)

## Development

### Prerequisites

-   Node.js (v14 or higher)
-   npm or yarn package manager

### Setup

1. Clone the repository
2. Install dependencies:

```bash
npm install
```

### Running the Application

1. Build the panels:

```bash
./create_panels.sh
```

2. Start the development server:

```bash
npm run dev
```

### Project Structure

-   `src/`: Source code directory
    -   `services/`: Core services including code generation and layout management
    -   `pages/`: Vue components for different pages
    -   `components/`: Reusable UI components

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

[Add your license information here]
