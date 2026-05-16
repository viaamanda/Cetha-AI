from fastapi import FastAPI
from app.api.endpoints.ocr import router as ocr_router
from app.api.endpoints.dashboard import router as dashboard_router
from app.api.endpoints.kategorisasi import router as kategorisasi_router
from app.api.endpoints.smartinsight import router as smartinsight_router
from app.api.endpoints.saranstok import router as saranstok_router

app = FastAPI(title="Cetha AI Backend")

app.include_router(ocr_router,        prefix="/api/ocr",        tags=["OCR"])
app.include_router(dashboard_router,  prefix="/api/dashboard",  tags=["Dashboard"])
app.include_router(kategorisasi_router, prefix="/api/kategorisasi", tags=["Kategorisasi"])
app.include_router(smartinsight_router, prefix="/api/insight",  tags=["Smart Insight"])
app.include_router(saranskot_router,  prefix="/api/stok",       tags=["Saran Stok"])

@app.get("/")
def root():
    return {"message": "Cetha AI Backend is running"}