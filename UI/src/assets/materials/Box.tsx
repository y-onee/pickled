import type { HTMLAttributes } from 'react';
import './Box.css';

type BoxProps = HTMLAttributes<HTMLDivElement>;

export const Box = ({ children, className, ...props }: BoxProps) => {
  return (
    <div
      className={`material-box${className ? ` ${className}` : ''}`}
      {...props}
    >
      {children}
    </div>
  );
};
