import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {Canh} from './scenes';
import {MAU, PHONG_CHU, PHONG_TIEU_DE} from './theme';

// Độ trễ giữa các mục xuất hiện: chia đều 70% thời lượng cảnh cho phần "diễn ra
// tuần tự", 30% còn lại để giữ nguyên trạng thái đã hoàn chỉnh cho lời đọc kết.
function doTre(fps: number, tongKhung: number, soMuc: number): number {
  const khungDanh = tongKhung * 0.7;
  return soMuc > 1 ? khungDanh / soMuc : khungDanh;
}

function hienRa(frame: number, batDauKhung: number, fps: number) {
  const f = spring({frame: frame - batDauKhung, fps, config: {damping: 18, stiffness: 120}});
  return {
    opacity: interpolate(f, [0, 1], [0, 1]),
    transform: `translateY(${interpolate(f, [0, 1], [18, 0])}px) scale(${interpolate(f, [0, 1], [0.92, 1])})`,
  };
}

const oChu: React.CSSProperties = {fontFamily: PHONG_CHU, color: MAU.chu};
const oTieuDe: React.CSSProperties = {
  fontFamily: PHONG_TIEU_DE,
  color: MAU.coralDam,
  fontSize: 44,
  fontWeight: 700,
  textAlign: 'center',
  margin: 0,
  padding: '0 40px',
};

const oHop: React.CSSProperties = {
  background: MAU.mat,
  border: `2px solid ${MAU.vien}`,
  borderRadius: 22,
  boxShadow: `7px 9px 20px rgba(172,77,51,.13)`,
  padding: '22px 20px',
  color: MAU.chu,
  fontFamily: PHONG_CHU,
  whiteSpace: 'pre-line',
  textAlign: 'center',
  lineHeight: 1.35,
};

function CanhFlow({items, nhieu}: {items: string[]; nhieu?: string}) {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const tre = doTre(fps, durationInFrames, items.length);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center'}}>
      {nhieu && (
        <div
          style={{
            position: 'absolute',
            top: '18%',
            ...hienRa(frame, tre * items.length + fps * 0.3, fps),
            background: MAU.vangNen,
            color: MAU.vang,
            border: `2px dashed ${MAU.vang}`,
            borderRadius: 16,
            padding: '10px 24px',
            fontFamily: PHONG_CHU,
            fontSize: 22,
            maxWidth: 780,
            textAlign: 'center',
          }}
        >
          {nhieu}
        </div>
      )}
      <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
        {items.map((it, i) => (
          <React.Fragment key={i}>
            <div style={{...oHop, width: 220, minHeight: 130, fontSize: 24, ...hienRa(frame, i * tre, fps)}}>
              {it}
            </div>
            {i < items.length - 1 && (
              <div style={{...hienRa(frame, i * tre + tre * 0.6, fps), fontSize: 40, color: MAU.coral}}>➜</div>
            )}
          </React.Fragment>
        ))}
      </div>
    </AbsoluteFill>
  );
}

function CanhLadder({items}: {items: string[]}) {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const tre = doTre(fps, durationInFrames, items.length);
  const n = items.length;
  return (
    <AbsoluteFill style={{alignItems: 'flex-end', justifyContent: 'center', padding: '0 90px 60px'}}>
      <div style={{display: 'flex', alignItems: 'flex-end', gap: 22, width: '100%', justifyContent: 'center'}}>
        {items.map((it, i) => {
          const cao = 90 + i * 62;
          return (
            <div
              key={i}
              style={{
                ...hienRa(frame, i * tre, fps),
                width: 168,
                height: cao,
                background: i === n - 1 ? MAU.chinh : MAU.coralNhat,
                color: i === n - 1 ? MAU.trenChinh : MAU.coralDam,
                borderRadius: '14px 14px 0 0',
                display: 'flex',
                alignItems: 'flex-start',
                justifyContent: 'center',
                paddingTop: 14,
                fontFamily: PHONG_CHU,
                fontWeight: i === n - 1 ? 700 : 500,
                fontSize: 19,
                textAlign: 'center',
              }}
            >
              <span style={{padding: '0 8px'}}>{`${i + 1}. ${it}`}</span>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
}

function CanhRange({traiNhan, phaiNhan, vungNhan}: {traiNhan: string; phaiNhan: string; vungNhan: string}) {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const traiF = spring({frame, fps, config: {damping: 20}});
  const phaiF = spring({frame: frame - fps * 0.3, fps, config: {damping: 20}});
  const vungOpac = interpolate(frame, [fps * 1.4, fps * 2.2], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const traiW = interpolate(traiF, [0, 1], [0, 55]);
  const phaiW = interpolate(phaiF, [0, 1], [0, 55]);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center'}}>
      <div style={{width: '78%', position: 'relative', height: 90}}>
        <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, right: 0, background: MAU.nenSau, borderRadius: 45}} />
        <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, width: `${traiW}%`, background: MAU.coralNhat, borderRadius: '45px 0 0 45px'}} />
        <div style={{position: 'absolute', right: 0, top: 0, bottom: 0, width: `${phaiW}%`, background: MAU.coralNhat, borderRadius: '0 45px 45px 0'}} />
        <div
          style={{
            position: 'absolute',
            left: `${Math.min(traiW, 100 - phaiW)}%`,
            width: `${Math.abs(traiW - (100 - phaiW))}%`,
            top: 0,
            bottom: 0,
            background: MAU.chinh,
            opacity: vungOpac,
          }}
        />
        <div style={{position: 'absolute', top: -60, left: 0, width: 260, ...oHop, fontSize: 20, opacity: traiF}}>{traiNhan}</div>
        <div style={{position: 'absolute', top: -60, right: 0, width: 260, ...oHop, fontSize: 20, opacity: phaiF}}>{phaiNhan}</div>
        <div
          style={{
            position: 'absolute',
            top: 110,
            left: `${Math.min(traiW, 100 - phaiW)}%`,
            transform: 'translateX(-20%)',
            opacity: vungOpac,
            color: MAU.coralDam,
            fontFamily: PHONG_TIEU_DE,
            fontWeight: 700,
            fontSize: 30,
          }}
        >
          {vungNhan}
        </div>
      </div>
    </AbsoluteFill>
  );
}

function CanhLayout({o}: {o: {nhan: string; x: number; y: number; w: number; h: number}[]}) {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const tre = doTre(fps, durationInFrames, o.length);
  const trangW = 420;
  const trangH = 500;
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 150}}>
      <div
        style={{
          position: 'relative',
          width: trangW,
          height: trangH,
          background: MAU.mat,
          border: `2px solid ${MAU.vien}`,
          boxShadow: '7px 9px 20px rgba(172,77,51,.13)',
        }}
      >
        {o.map((z, i) => (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: `${z.x}%`,
              top: `${z.y}%`,
              width: `${z.w}%`,
              height: `${z.h}%`,
              border: `2px solid ${MAU.chinh}`,
              background: MAU.chinhNen,
              borderRadius: 6,
              ...hienRa(frame, i * tre, fps),
            }}
          />
        ))}
      </div>
      <div style={{position: 'absolute', right: 70, top: 165, width: 340, display: 'flex', flexDirection: 'column', gap: 14}}>
        {o.map((z, i) => (
          <div key={i} style={{...oChu, fontSize: 18, ...hienRa(frame, i * tre, fps)}}>
            <b style={{color: MAU.chinh}}>{i + 1}.</b> {z.nhan}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
}

function CanhChecklist({items}: {items: string[]}) {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const tre = doTre(fps, durationInFrames, items.length);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center'}}>
      <div style={{display: 'flex', flexDirection: 'column', gap: 16}}>
        {items.map((it, i) => {
          const f = spring({frame: frame - i * tre, fps, config: {damping: 16}});
          return (
            <div key={i} style={{display: 'flex', alignItems: 'center', gap: 18, opacity: interpolate(f, [0, 1], [0, 1])}}>
              <div
                style={{
                  width: 40,
                  height: 40,
                  borderRadius: '50%',
                  background: interpolate(f, [0, 1], [0, 1]) > 0.5 ? MAU.dung : MAU.mat,
                  border: `2px solid ${MAU.dung}`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: MAU.trenChinh,
                  fontSize: 22,
                  transform: `scale(${interpolate(f, [0, 1], [0.4, 1])})`,
                }}
              >
                {f > 0.5 ? '✓' : ''}
              </div>
              <div style={{...oChu, fontSize: 26}}>{it}</div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
}

function CanhGrid({items}: {items: {nhan: string; chiTiet: string}[]}) {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const tre = doTre(fps, durationInFrames, items.length);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center'}}>
      <div style={{display: 'flex', gap: 18}}>
        {items.map((it, i) => {
          const f = spring({frame: frame - i * tre, fps, config: {damping: 20}});
          const lat = interpolate(f, [0, 1], [0, 180]);
          return (
            <div
              key={i}
              style={{
                width: 190,
                height: 230,
                perspective: 800,
              }}
            >
              <div
                style={{
                  width: '100%',
                  height: '100%',
                  transformStyle: 'preserve-3d',
                  transform: `rotateY(${lat}deg)`,
                  position: 'relative',
                }}
              >
                <div
                  style={{
                    position: 'absolute',
                    inset: 0,
                    backfaceVisibility: 'hidden',
                    background: MAU.chinh,
                    borderRadius: 18,
                  }}
                />
                <div
                  style={{
                    position: 'absolute',
                    inset: 0,
                    backfaceVisibility: 'hidden',
                    transform: 'rotateY(180deg)',
                    background: MAU.mat,
                    border: `2px solid ${MAU.vien}`,
                    borderRadius: 18,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: 16,
                    gap: 10,
                    textAlign: 'center',
                  }}
                >
                  <div style={{fontFamily: PHONG_TIEU_DE, color: MAU.coralDam, fontWeight: 700, fontSize: 22}}>{it.nhan}</div>
                  <div style={{...oChu, fontSize: 15}}>{it.chiTiet}</div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
}

export const Scene: React.FC<{canh: Canh}> = ({canh}) => {
  return (
    <AbsoluteFill style={{background: MAU.nen}}>
      <div style={{position: 'absolute', top: 36, left: 0, right: 0, display: 'flex', justifyContent: 'center'}}>
        <h1 style={oTieuDe}>{canh.title}</h1>
      </div>
      {canh.kind === 'flow' && <CanhFlow items={canh.items} nhieu={canh.nhieu} />}
      {canh.kind === 'ladder' && <CanhLadder items={canh.items} />}
      {canh.kind === 'range' && <CanhRange traiNhan={canh.traiNhan} phaiNhan={canh.phaiNhan} vungNhan={canh.vungNhan} />}
      {canh.kind === 'layout' && <CanhLayout o={canh.o} />}
      {canh.kind === 'checklist' && <CanhChecklist items={canh.items} />}
      {canh.kind === 'grid' && <CanhGrid items={canh.items} />}
    </AbsoluteFill>
  );
};
