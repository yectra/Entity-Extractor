from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy

app = FastAPI()

class EntityExtractionRequest(BaseModel):
    text: str

@app.post("/extract-entities")
def extract_entities(request: EntityExtractionRequest):
    try:
        # Load the English language model from SpaCy
        nlp = spacy.load("en_core_web_sm")
        
        # Process the text using the loaded model
        doc = nlp(request.text)
        
        # Extract entities from the processed text
        entities = [{"text": ent.text, "type": ent.label_} for ent in doc.ents]
        
        # Calculate counts of different types of entities
        entity_counts = count_entities(entities)
        
        # Return the extracted entities along with counts
        response = {
            "entities": entities,
            "entity_counts": entity_counts
        }
        return response
    except Exception as e:
        # If an error occurs during processing, return an HTTP 500 error
        raise HTTPException(status_code=500, detail=str(e))

def count_entities(entities):
    # Initialize counts for different types of entities
    entity_counts = {
        "PERSON": 0,
        "ORG": 0,
        "LOC": 0,
        "DATE": 0,
        "TIME": 0,
        "MONEY": 0,
        "PERCENT": 0,
        "CARDINAL": 0,
        "ORDINAL": 0,
        "QUANTITY": 0,
        "LANGUAGE": 0,
        "EVENT": 0,
        "NORP": 0
        # Add more entity types as needed
    }
    
    # Count occurrences of each entity type
    for entity in entities:
        entity_type = entity["type"]
        if entity_type in entity_counts:
            entity_counts[entity_type] += 1
    
    return entity_counts
