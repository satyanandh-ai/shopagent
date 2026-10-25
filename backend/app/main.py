from fastapi import FastAPI

app = FastAPI(
    title="ShopAgent API",
    description="Backend API for the ShopAgent project",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
