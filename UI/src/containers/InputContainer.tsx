import { useState, type FormEvent } from 'react';
import { Box } from '../assets/materials/Box';
import { InputFields } from '../components/InputFields';

const storageKey = 'pickled-sessions';

export const InputContainer = () => {
  const [players, setPlayers] = useState('');
  const [sessions, setSessions] = useState('');
  const [error, setError] = useState('');
  const [history, setHistory] = useState<string[]>(() => {
    const stored = localStorage.getItem(storageKey);
    return stored ? (JSON.parse(stored) as string[]) : [];
  });

  const generateSchedule = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError('');

    const playerCount = Number(players);
    const sessionCount = Number(sessions);
    if (!Number.isInteger(playerCount) || playerCount < 4 || playerCount > 26) {
      setError('Enter a player count from 4 to 26.');
      return;
    }
    if (!Number.isInteger(sessionCount) || sessionCount < 1) {
      setError('Enter a positive number of sessions.');
      return;
    }

    try {
      const response = await fetch('/api/schedule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ players: playerCount, sessions: sessionCount }),
      });
      const result = await response.json();
      if (!response.ok) {
        throw new Error(result.error ?? 'Could not generate the schedule.');
      }

      const updatedHistory = [...history, result.output];
      localStorage.setItem(storageKey, JSON.stringify(updatedHistory));
      setHistory(updatedHistory);
    } catch (requestError) {
      setError(
        requestError instanceof Error
          ? requestError.message
          : 'Could not generate the schedule.',
      );
    }
  };

  return (
    <Box
      style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
      }}
    >
      <form onSubmit={generateSchedule}>
        <InputFields
          textName="Players: "
          fieldName="players"
          value={players}
          onChange={setPlayers}
        />
        <InputFields
          textName="Sessions: "
          fieldName="sessions"
          value={sessions}
          onChange={setSessions}
        />
        <button type="submit">Generate</button>
      </form>

      {error && <p role="alert">{error}</p>}
      {history.map((result, index) => (
        <pre key={index}>{result}</pre>
      ))}
    </Box>
  );
};
