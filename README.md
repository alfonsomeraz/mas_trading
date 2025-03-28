┌────────────────────────┐
│   CLI Entry Point      │
└────────────────────────┘
           ↓
┌────────────────────────┐
│   Agent Orchestrator   │  ← CrewAI / Ray / LangChain
└────────────────────────┘
     ↓        ↓         ↓
  News      Macro     Sentiment  ← Use GPU for inference or embeddings
   ↓          ↓          ↓
         Thesis Generator
                ↓
          Ticker Watchlist
                ↓
        Output to CLI / Web
