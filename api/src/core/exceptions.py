from fastapi import HTTPException

def raise_not_found(entity: str, identifier : str | int ) -> None :
    raise HTTPException(status_code=404, detail=f"{entity} {identifier} not found ! ")

def raise_conflict(message : str ) ->  None : 
    raise HTTPException(status_code=400, detail = message )