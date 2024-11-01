# zomboid

The world is on the brink of a new epidemic. The disease Z32-19 causes irreversible damage to the central nervous system. The main symptoms include: increased aggressiveness, blurred vision, reduced intelligence, hunger and thirst. The disease also causes the body to produce stem cells uncontrollably.
**This app is for the survivor community that helps
keep records of essential items.**

## Class diagrams

```mermaid
classDiagram
class DataModel{
    +str id
    +str name
    +str type_object
    +str condition
    +str amount
    *get_dict_data_models() Dict~str, int~
}
class AbstractReader{
    *read() List~DataModel~ 
    *get_header() Dict~str, int~ 
}
class PrinterModel{
    +List~DataModel~ data_model
    +Dict~str, int~ heads_table
    *print() void
}
class SeparatorModel{
    +List~DataModel~ data_models
    +int skip
    +int take
    *get_models() List~DataModel~
}
class Zomboid{
    +List~DataModel~ data_model
    +Dict~str, int~ dic_model
    *print_models() void
}
class CSVReader{
    +Path Path
    +Dict~str, int~ dic_header
}
class XMLReader{
    +Path Path
    +Dict~str, int~ dic_header
    +str tree_root
}
class JSONReader{
    +Path path
    +Dict~str, int~ dic_header
}
AbstractReader <| -- CSVReader
AbstractReader <| -- XMLReader
AbstractReader <| -- JSONReader

```
