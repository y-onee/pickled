import { useState } from 'react';
import { Box } from '../assets/materials/Box';
import { InputFields } from '../components/InputFields';

export const InputContainer = () => {
  const [players, setPlayers] = useState('');
  const [sessions, setSessions] = useState('');

  return (
    <Box style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
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
    </Box>
  );
};
