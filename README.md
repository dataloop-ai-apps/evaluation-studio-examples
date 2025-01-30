# Form Schema Documentation

This documentation outlines the capabilities and components available in the form schema system. The system supports rich, interactive forms with various layouts and component types.

## Schema Structure

Forms are defined using JSON schema arrays, where each form consists of sections containing components:

```json
[
    {
        "title": "Section Title",
        "layout": { 
            "direction": "horizontal|vertical",
            "wrap": true|false 
        },
        "components": [
            // components go here
        ]
    }
]
```

## Layouts

### Section Layouts

- **Vertical** (default): Components stack vertically
- **Horizontal**: Components align horizontally
  - `wrap`: Controls whether components wrap to next line
  - Example: `"layout": { "direction": "horizontal", "wrap": true }`

## Components

### Text Input
```json
{
    "type": "text",
    "key": "field_name",
    "title": "Display Title",
    "placeholder": "Placeholder text",
    "tooltip": "Helper text shown on hover",
    "allowStatus": true  // Optional: Enables status updates
}
```

### Radio Buttons
```json
{
    "type": "radio",
    "key": "choice_field",
    "title": "Question Title",
    "default": false,
    "allowStatus": true,  // Optional
    "options": [
        { "label": "Option 1", "value": true },
        { "label": "Option 2", "value": false }
    ]
}
```

### Select Dropdown
```json
{
    "type": "select",
    "key": "dropdown_field",
    "title": "Dropdown Title",
    "placeholder": "Select an option",
    "tooltip": "Helper text",
    "options": [
        { "label": "Option 1", "value": "value1" },
        { "label": "Option 2", "value": "value2" }
    ]
}
```

### Slider
```json
{
    "type": "slider",
    "key": "slider_field",
    "title": "Slider Title",
    "min": -999999999,
    "max": 999999999,
    "step": 100000000,
    "placeholder": "Slider placeholder"
}
```

### Media Components

#### Image
```json
{
    "type": "image",
    "key": "image_field",
    "title": "Image Title"
}
```

#### Video
```json
{
    "type": "video",
    "key": "video_field",
    "title": "Video Title"
}
```

#### Audio
```json
{
    "type": "audio",
    "key": "audio_field",
    "title": "Audio Title"
}
```

## Advanced Features

### Hierarchical Dependencies
Components can be conditionally shown based on parent field values:
```json
{
    "type": "text",
    "key": "conditional_field",
    "title": "Conditional Field",
    "hierarchy": {
        "parentLabel": "parent_field",
        "parentValue": true
    }
}
```

### Status Updates
Components can support status updates by adding `"allowStatus": true`

## Example Use Cases

### 1. Basic Form
See `examples/simple-prompt-response/` for a basic form implementation.

### 2. Two-Section Vertical Layout
See `examples/two-sections-vertical/` for a form with multiple vertical sections.

### 3. Media Form
See `examples/form-with-binary-files/` for handling images, videos, and audio.

### 4. Hierarchical Form
See `examples/with-hierarchy/` for forms with conditional fields.

### 5. Status-Enabled Form
See `examples/with-status-update/` for forms with status update capabilities.

## Response Format

Form responses should match the schema structure using the defined keys. Example:

```json
{
    "field_key": "field_value",
    "another_key": "another_value"
}
```

## Best Practices

1. Use meaningful keys that reflect the data being collected
2. Provide clear titles and tooltips for better user experience
3. Use appropriate component types for the data being collected
4. Consider mobile responsiveness when using horizontal layouts
5. Use hierarchical dependencies sparingly to maintain form simplicity
