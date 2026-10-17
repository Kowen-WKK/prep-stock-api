  CREATE TABLE items (
      id         SERIAL PRIMARY KEY,
      name       TEXT NOT NULL,
      quantity   NUMERIC NOT NULL DEFAULT 0,
      created_at TIMESTAMPTZ DEFAULT now()
  );