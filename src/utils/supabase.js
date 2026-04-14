import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm';

export const SUPABASE_URL  = 'https://jgytwvtdqpotdaleotok.supabase.co';
export const SUPABASE_ANON = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impne' +
  'XR3dnRkcXBvdGRhbGVvdG9rIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYwMDYzMTYsImV4cCI6MjA5MT' +
  'U4MjMxNn0.to6i9_FY33IjcIyY1ETy-mkmlm6kSOujyKNoo7_v2BA';

export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON);
