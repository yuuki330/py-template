# DDD Architecture

Layers under src/: domain/, application/, infrastructure/, presentation/.
Direction: Presentation -> Application -> Domain <- Infrastructure.
Directory names are flexible per project; dependency rules are fixed.
Layer-specific import rules load automatically when working with files in each layer directory.
