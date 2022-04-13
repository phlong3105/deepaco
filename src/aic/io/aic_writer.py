#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""IO classes especially for AI City Challenge tasks.
"""

from __future__ import annotations

import os
from operator import itemgetter
from pathlib import Path
from timeit import default_timer as timer
from typing import Optional

from aic.objects import Product
from onevision import console
from onevision import create_dirs
from onevision import is_stem

__all__ = [
	"AIC22RetailCheckoutWriter",
]


# MARK: - AIC22RetailCheckoutWriter

class AIC22RetailCheckoutWriter:
	"""AIC Retail Checkout Writer periodically saves the detection results in ONE
	camera.
	
	Attributes:
		dst (str):
			Path to the file to save the counting results.
		camera_name (str):
			Camera name.
		video_id (int):
			Numeric identifier of input camera stream.
		start_time (float):
			Moment when the TexIO is initialized.
		writer (io stream):
			File writer to export the counting results.
	"""
	
	# Numeric identifier of input camera stream
	video_map = {
		"testA_1": 1,
		"testA_2": 2,
		"testA_3": 3,
		"testA_4": 4,
		"testA_5": 5,
	}
	
	# MARK: Magic Function

	def __init__(
		self,
		dst 	   : str,
		camera_name: str,
		start_time : float = timer(),
		*args, **kwargs
	):
		super().__init__()
		if camera_name not in self.video_map:
			raise ValueError(
				f"The given `camera_name` has not been defined in AIC camera "
			    f"list. Please check again!"
			)

		self.dst		 = dst
		self.camera_name = camera_name
		self.video_id 	 = self.video_map[camera_name]
		self.start_time  = start_time
		self.lines 		 = []
		# self.init_writer(dst=self.dst)
		
	def __del__(self):
		""" Close the writer object."""
		"""
		if self.writer:
			self.writer.close()
		"""
		pass

	# MARK: Configure

	def init_writer(self, dst: str):
		"""Initialize writer object.

		Args:
			dst (str):
				Path to the file to save the counting results.
		"""
		if is_stem(dst):
			dst = f"{dst}.txt"
		elif os.path.isdir(dst):
			dst = os.path.join(dst, f"{self.camera_name}.txt")
		parent_dir = str(Path(dst).parent)
		create_dirs(paths=[parent_dir])
		# self.writer = open(dst, "w")

	# MARK: Write
	
	def write(self, moving_objects: list[Product]):
		"""Write counting result from a list of tracked moving objects.
		
		Each line in the output format of AI City Challenge contains:
		<gen_time> <video_id> <frame_id> <MOI_id> <vehicle_class_id>
			<gen_time>:         [float] is the generation time until this
										frame’s output is generated, from the
										start of the program execution, in
										seconds.
			<video_id>:         [int] is the video numeric identifier, starting
									  with 1.
			<frame_id>:         [int] represents the frame count for the
									  current frame in the current video,
									  starting with 1.
			<MOI_id>:           [int] denotes the the movement numeric
									  identifier of the movement of that video.
			<vehicle_class_id>: [int] is the road_objects classic numeric
									  identifier, where 1 stands for “car”
									  and 2 represents “truck”.
		
		Args:
			moving_objects (list):
				List of tracked moving objects.
		"""
		for obj in moving_objects:
			class_id = obj.label_id_by_majority
			if class_id != 116:
				# line = f"{self.video_id} {class_id + 1} {int(obj.timestamp)} {obj.label_by_majority.name}\n"
				line = f"{self.video_id} {class_id + 1} {int(obj.timestamp)}\n"
				self.lines.append(line)
				# self.writer.write(line)
	
	def dump(self):
		dst = self.dst
		if is_stem(dst):
			dst = f"{dst}.txt"
		elif os.path.isdir(dst):
			dst = os.path.join(dst, f"{self.camera_name}.txt")
		parent_dir = str(Path(dst).parent)
		create_dirs(paths=[parent_dir])
		
		with open(dst, "w") as f:
			for line in self.lines:
				f.write(line)
	
	@classmethod
	def compress_all_results(
		cls,
		output_dir : Optional[str] = None,
		output_name: Optional[str] = None
	):
		"""Compress all result of video into one file
		
		Args:
			output_dir (str):
				Directory of output track1.txt will be written
			output_name:
				Final compress result name
					e.g.: "track1.txt"
		"""
		output_dir 		= output_dir  if (output_dir is not None)  else ""
		output_name 	= output_name if (output_name is not None) else "track4"
		output_name 	= os.path.join(output_dir, f"{output_name}.txt")
		compress_writer = open(output_name, "w")
	
		# NOTE: Get result from each file
		for video_name, video_id in cls.video_map.items():
			video_result_file = os.path.join(output_dir, f"{video_name}.txt")
	
			if not os.path.exists(video_result_file):
				console.log(f"Result of {video_result_file} is not exist")
				continue
	
			# NOTE: Read result
			results = []
			with open(video_result_file) as f:
				line = f.readline()
				while line:
					words  = line.split(" ")
					result = {
						"video_id" : int(words[0]),
						"class_id" : int(words[1]),
						"timestamp": int(words[2]),
					}
					if result["class_id"] != 116:
						results.append(result)
					line = f.readline()
	
			# NOTE: Sort result
			results = sorted(results, key=itemgetter("video_id"))
	
			# NOTE: write result
			for result in results:
				compress_writer.write(f"{result['video_id']} ")
				compress_writer.write(f"{result['class_id']} ")
				compress_writer.write(f"{result['timestamp']} ")
				compress_writer.write("\n")
	
		compress_writer.close()
