type InputFieldsProps = {
  fieldName: string;
  textName: string;
  value: string;
  onChange: (value: string) => void;
};

export const InputFields = ({
  fieldName,
  textName,
  value,
  onChange,
}: InputFieldsProps) => {
  return (
    <label>
      {textName}
      <input
        type="text"
        name={fieldName}
        value={value}
        onChange={(event) => onChange(event.target.value)}
      />
    </label>
  );
};
