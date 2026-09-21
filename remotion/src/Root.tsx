import React from 'react';
import {CalculateMetadataFunction, Composition} from 'remotion';
import {Scene} from './Scene';
import {CANH, Canh} from './scenes';

// Kích thước và khung hình khớp với video tĩnh sinh bởi scripts/build_videos.py
// (ffmpeg -framerate 25, 1280x720) để hai loại đoạn nối liền mạch khi ghép.
const FPS = 25;
const RONG = 1280;
const CAO = 720;

type Props = {
  sceneId: string;
  seconds: number;
  canh?: Canh;
};

// Thời lượng thật của mỗi cảnh chỉ biết được sau khi Piper đọc xong lời thoại,
// nên build_videos.py truyền `seconds` qua --props và ta tính lại số khung ở đây
// thay vì đặt cố định trên <Composition>.
const tinhSo: CalculateMetadataFunction<Props> = ({props}) => {
  const canh = CANH[props.sceneId];
  if (!canh) {
    throw new Error(`scenes.ts không có sceneId "${props.sceneId}"`);
  }
  return {
    durationInFrames: Math.max(1, Math.round(props.seconds * FPS)),
    props: {...props, canh},
  };
};

const CanhTuProps: React.FC<Props> = (props) => <Scene canh={props.canh ?? CANH[props.sceneId]} />;

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Canh"
      component={CanhTuProps}
      fps={FPS}
      width={RONG}
      height={CAO}
      durationInFrames={FPS * 5}
      defaultProps={{sceneId: 'c1', seconds: 5}}
      calculateMetadata={tinhSo}
    />
  );
};
