from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola DevOps, todo gratis :)"}

@app.get("/health")
def health():
    return {"status": "ok"}

print("trigger CI")
print("trigger CI6")

